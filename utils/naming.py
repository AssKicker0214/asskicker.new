import random as rd
import string
import time
import os


def random_token(length=16):
    population = string.ascii_letters + string.digits
    return ''.join([rd.choice(population) for _ in range(length)])


def random_img_name(parent_dir=None):
    """
    To name the uploaded imaged, the name starts with `img`, followed by
    `date` and a random string
    :return:
    """
    population = string.digits + string.digits
    prefix_seg = 'img'
    date_seg = time.strftime("%Y-%m-%d")
    random_seg = ''.join([rd.choice(population) for _ in range(4)])
    img_name = "%s_%s_%s" % (prefix_seg, date_seg, random_seg)
    return img_name if parent_dir is None else os.path.join(parent_dir, img_name)
