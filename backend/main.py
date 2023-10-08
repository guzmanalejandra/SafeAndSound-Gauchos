from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from PIL import Image
from logic.scanImage import getNotesFromImage
from logic.sound import procesarNotas
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
    # print(imagen)
    # remove data:
    imagen = imagen.replace("data:image/jpeg;base64,", "")
    imagen = imagen.replace("data:image/png;base64,", "")
    imagen = imagen.replace("data:image/jpg;base64,", "")
    
    imgdata = base64.b64decode(imagen)
    filename = 'image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    
    img = Image.open(filename)
    img.resize((140,140))
    notes = getNotesFromImage(img)
    song = procesarNotas(notes)
    song.export("song.wav", format="wav")
    
    # return json with ok
    return jsonify({'status': 'ok'})

@app.route('/getSong', methods=['GET'])
def getSong():
    return send_file('song.wav', mimetype='audio/wav')


if __name__ == '__main__':
    app.run(debug=True)
    
