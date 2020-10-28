from requests import get
from os.path import dirname, realpath, exists
from os import mkdir

script_dir = realpath(dirname(__file__))
assets_dir = '{0}/assets'.format(dirname(script_dir))

if not exists(assets_dir):
    mkdir(assets_dir)

file_list = {
    'biden01.jpg': 'https://s.abcnews.com/images/Politics/joe-biden-town-hall-04-abc-jc-201015_1602807301650_hpMain_16x9_1600.jpg',
    'biden02.jpg': 'https://media1.s-nbcnews.com/i/newscms/2020_13/3287981/200329-joe-biden-mtp-cs-1109a_e5c3be75eec1e1e4be33556441516a3d.jpg'
}

for file in file_list.keys():
    target_path = '{0}/{1}'.format(assets_dir, file)
    with open(target_path, 'wb') as target:
        target.write(get(file_list[file]).content)
        print('Downloaded file {0}'.format(file))