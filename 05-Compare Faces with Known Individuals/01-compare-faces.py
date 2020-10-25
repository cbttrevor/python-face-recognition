from face_recognition import compare_faces, load_image_file, face_encodings
from os.path import dirname, realpath
from glob import glob

script_dir = dirname(realpath(__file__))

# Load the face of someone we "know about"
known_face_path = '{0}/assets/president01.jpg'.format(dirname(script_dir))
known_face = load_image_file(known_face_path)

trump_face = face_encodings(known_face)[0]
print(trump_face)

for file in glob('{0}/assets/*.jpg'.format(dirname(script_dir))):
    current_image = load_image_file(file)
    for encoding in face_encodings(current_image):
        # print(encoding)
        print(compare_faces([trump_face], encoding, tolerance=0.8))
    # face_recognition.compare_faces()