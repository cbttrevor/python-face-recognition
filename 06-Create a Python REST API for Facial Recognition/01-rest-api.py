from flask import Flask, request
from face_recognition import load_image_file, face_locations
import requests
from uuid import uuid4
from os.path import dirname, realpath

script_dir = dirname(realpath(__file__))
app = Flask(__name__)

@app.route('/detect', methods=['POST', 'GET'])
def detect_faces():
    file = requests.get(request.data)
    file_extension = request.data.decode('utf-8').split('.')[-1]
    temp_file_name = '{0}/{1}.{2}'.format(script_dir, uuid4(), file_extension)
    print('Temp file name is: {0}'.format(temp_file_name))
    with open(temp_file_name, 'wb') as target_file:
        target_file.write(file.content)
    
    # Load the image from the filesystem and detect faces
    img = load_image_file(temp_file_name)
    return 'We found {0} faces'.format(len(face_locations(img)))

app.run(port=3001)