class Sound:
    def __init__(self):
        self.CardSound = ''
        self.TableSound = ''
        self.WinSound = ''
        self.LoseSound = ''

    def playSound(self, sound_type):
        if sound_type == 'card':
            return self.CardSound
        elif sound_type == 'table':
            return self.TableSound
        elif sound_type == 'win':
            return self.WinSound
        elif sound_type == 'lose':
            return self.LoseSound
