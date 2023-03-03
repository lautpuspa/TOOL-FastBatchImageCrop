import glob
import os
import sys
import errno
import json
from PIL import Image

ERROR_INVALID_NAME = 123


def get_image_files(path):
    types = ('*.jpg', '*.JPG', '*.jpeg', '*.JPEG', '*.png', '*.PNG' '*.webp', '*.WEBP')
    filepaths = []
    filenames = []
    for t in types:
        filepaths.extend(glob.glob(path + '/' + t))

    filepaths = sorted(filepaths)

    for file in filepaths:
        head, tail = os.path.split(file)
        filenames.append(tail)

    return tuple(zip(filenames, filepaths))


def save_image_to_file(image: Image, filepath=None):
    create_folder(os.path.dirname(os.path.abspath(filepath)))
    image.save(filepath, quality=100, optimize=True)

    
def save_image_description_to_file(description=None, filepath=None):
    if description is not None:
        create_folder(os.path.dirname(os.path.abspath(filepath)))
        text_file = open(filepath, "w")
        n = text_file.write(description)
        text_file.close()

def load_tag_data(filename):
    tag_data = None
    tag_data_filename = filename+'.tagdata'
    if os.path.exists(tag_data_filename):
        with open(tag_data_filename, "r") as f:
            data = f.read()
            tag_data = json.loads(data)

    return tag_data

def save_tag_data(filename, tag_data):
    tagdata_filename = filename+'.tagdata'
    with open(tagdata_filename, "w") as f:
        json_str = json.dumps(tag_data, sort_keys=False, indent=4)
        f.write(json_str)


def check_path_valid(path) -> bool:
    try:
        if not isinstance(path, str) or not path:
            return False

        _, path = os.path.splitdrive(path)

        root_dirname = os.environ.get('HOMEDRIVE', 'C:') if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)

        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        for pathname_part in path.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False

    except TypeError as exc:
        return False

    else:
        return True


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
