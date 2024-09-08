from flask import Flask, send_from_directory, send_file, abort

app = Flask(__name__, static_folder='build/web')

# Serve the index.html at the root URL
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve any other file in the build/web directory
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/archives/repo/<version>/<filename>', methods=['GET'])
def download_file(version, filename):
    # Construct the file path based on the parameters
    file_path = 'build/web/whl'

    try:
        # Send the file to the client
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        # Handle the case where the file is not found
        abort(404, description="Resource not found")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
