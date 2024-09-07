from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    # Serve the image located in the 'static' folder
    return send_from_directory('resources/', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
