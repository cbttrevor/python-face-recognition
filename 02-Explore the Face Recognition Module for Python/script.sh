# Install Python3, pip3, and cmake
# NOTE: cmake is required to build dlib
apt update && apt install python3-pip cmake --yes

# Search for face recognition modules on PyPi
pip3 search face

# Install the face-recognition module from PyPi
pip3 install face-recognition opencv-python

# Run the command line utility
face_recognition --help