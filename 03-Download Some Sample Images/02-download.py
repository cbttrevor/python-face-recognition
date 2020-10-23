import requests
import os

# Get the absolute path of the directory containing the script file
script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir)

# Create a shared assets folder for the project
assets_folder = '{0}/../assets'.format(script_dir)
if (os.path.exists(assets_folder) == False):
    os.mkdir(assets_folder)

# Define a series of files to retrieve
file_list = {
    'president01.jpg': 'https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg',
    'president02.jpg': 'https://static01.nyt.com/images/2020/04/27/us/politics/00-trump-cand-page/00-trump-cand-page-mediumSquareAt3X.jpg',
    'president03.jpg': 'https://storage.googleapis.com/afs-prod/media/7d66df6467bb4c15944a41f36e2dc479/800.jpeg'
}

# Download the files locally to the assets folder
for file in file_list.keys():
    target_path = '{0}/{1}'.format(assets_folder, file)
    print('Downloading image from {0} to {1}'.format(file_list[file], target_path))
    with open(target_path, 'wb') as target:
        result = requests.get(file_list[file])
        target.write(result.content)

