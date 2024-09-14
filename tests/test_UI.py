import unittest
from unittest.mock import Mock, patch
from src.UI import UI


class TestUI(unittest.TestCase):

    def setUp(self):

        self.mock_dealer = Mock()
        self.mock_sprite_factory = Mock()
        self.mock_display_surface = Mock()
        self.mock_card = Mock()

        patcher1 = patch('pygame.display.set_mode', return_value=self.mock_display_surface)
        patcher2 = patch('pygame.display.flip')
        patcher3 = patch('pygame.time.Clock')
        patcher4 = patch('src.SpriteFactory.SpriteFactory', return_value=self.mock_sprite_factory)

        self.addCleanup(patcher1.stop)
        self.addCleanup(patcher2.stop)
        self.addCleanup(patcher3.stop)
        self.addCleanup(patcher4.stop)

        self.mock_set_mode = patcher1.start()
        self.mock_flip = patcher2.start()
        self.mock_clock = patcher3.start()
        self.mock_sprite_factory_cls = patcher4.start()

        self.ui = UI(self.mock_dealer)

    def test_set_background(self):
        background_color = (255, 255, 255)  # White
        self.ui.set_background(background_color)
        self.mock_display_surface.fill.assert_called_once_with(background_color)

    def test_set_display_surf(self):
        self.ui.set_display_surf()
        self.mock_set_mode.assert_called()

    def test_get_display_surf(self):
        self.assertEqual(self.ui.get_display_surf(), self.mock_display_surface)

    def test_change_display_surface_color_green(self):
        self.ui.change_display_surface_color("GREEN")
        self.mock_display_surface.fill.assert_called_once_with(self.ui.GREEN)
        self.mock_flip.assert_called_once()

    def test_change_display_surface_color_blue(self):
        self.ui.change_display_surface_color("BLUE")
        self.mock_display_surface.fill.assert_called_once_with(self.ui.BLUE)
        self.mock_flip.assert_called_once()

    def test_change_display_surface_color_invalid(self):
        with self.assertRaises(Exception) as context:
            self.ui.change_display_surface_color("YELLOW")
        self.assertEqual(str(context.exception), "Invalid color passed to UI")

    def test_set_screen_width(self):
        new_width = 1280
        self.ui.set_screen_width(new_width)
        self.assertEqual(self.ui.screen_width, new_width)

    def test_set_screen_height(self):

        new_height = 720
        self.ui.set_screen_height(new_height)
        self.assertEqual(self.ui.screen_height, new_height)

    def test_set_game_window_caption(self):

        caption = "Jack Change It"
        with patch('pygame.display.set_caption') as mock_set_caption:
            self.ui.set_game_window_caption(caption)
            mock_set_caption.assert_called_once_with(caption)

    def test_update_display(self):

        mock_sprite_group = Mock()
        self.mock_sprite_factory.get_sprite_group.return_value = mock_sprite_group

        mock_card = Mock()
        self.ui.ui_sprites = mock_sprite_group

        self.ui.update_display(mock_card)
        mock_sprite_group.add.assert_called_once_with(mock_card)
        mock_sprite_group.draw.assert_called_once_with(self.mock_display_surface)
        self.mock_flip.assert_called_once()

    def test_draw_starting_cards(self):

        self.mock_dealer.get_player1_cards.return_value = ['2H', 'AH']
        self.ui.draw_card = Mock()

        self.ui.draw_starting_cards()

        self.ui.draw_card.assert_any_call('2H', True, 0)
        self.ui.draw_card.assert_any_call('AH', True, 1)