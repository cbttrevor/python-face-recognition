from os.path import realpath, dirname
from glob import glob
import face_recognition
import cv2
from functools import reduce

# Find the script's current directory
script_dir = realpath(dirname(__file__))
assets_dir = '{0}/assets'.format(dirname(script_dir))
print(assets_dir)

# Find all files with .jpg file extension in the ../assets/ directory
file_list = glob('{0}/*.jpg'.format(assets_dir))

# Print out the list of files
print(file_list)

for file in file_list:
    img = face_recognition.load_image_file(file)

    # Learning point: face locations are returned as arrays
    locations = face_recognition.face_locations(img)
    print(locations)
    for face_rect in locations:
        print(face_rect)
        cv2.rectangle(img, (face_rect[3], face_rect[0]), (face_rect[1], face_rect[2]), (0,0,255))

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('{0}-output.jpg'.format(file), img)