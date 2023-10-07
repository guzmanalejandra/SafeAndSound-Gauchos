from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image

app = Flask(__name__)
CORS(app)

# Define your routes here
@app.route('/')
def hello_world():
    return 'Hello from backend!'
# Example of a route that accepts POST requests

@app.route('/computeImage', methods=['POST'])
def computeImage():
    data = request.get_json()
    imagen = data['imgBase64']
    
    # convert the base64 string to image
    img = Image.open(imagen)
    
    return jsonify({'result': imagen})

if __name__ == '__main__':
    app.run(debug=True)