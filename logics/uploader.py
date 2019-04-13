from werkzeug.datastructures import FileStorage
import utils.config as conf
import utils.naming as naming
import os

img_dir_root, img_url_root = conf.img_uploading()


def upload_img(img: FileStorage) -> str or False:
    suffix = img.filename.split('.')[-1]
    target_name = naming.random_img_name() + '.' + suffix
    target_path = img_dir_root + target_name
    target_url = img_url_root + target_name
    img.save(target_path)
    return target_url if os.path.isfile(target_path) else False


