from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='build/web')

# Serve the index.html at the root URL
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve any other file in the build/web directory
@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
