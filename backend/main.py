from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from logic.scanImage import getNotesFromImage
import base64

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
    # remove data:
    imagen = imagen.replace("data:image/jpeg;base64,", "")
    imgdata = base64.b64decode(imagen)
    filename = 'image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    img = Image.open(filename)
    notes = getNotesFromImage(img)
    print(notes)
    return jsonify({'result': imagen})

if __name__ == '__main__':
    app.run(debug=True)