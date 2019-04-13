import os
import json

with open("config.json", encoding='utf-8') as f:
    conf = json.load(f)


def expose_port():
    return conf['port']


def passwd_hash():
    return conf['hashed']


def db_location():
    db_conf = conf['db']
    return {'host': db_conf['host'], 'port': db_conf['port']}


def article_collection():
    return conf['db']['article']['db_name'], conf['db']['article']['collection_name']


def security():
    return not conf['no_security']


def img_uploading() -> (str, str):
    dir_root = conf['upload']['img']['dir_root']
    if not os.path.isdir(dir_root):
        os.makedirs(dir_root)
    url_root = conf['upload']['img']['url_root']
    return dir_root, url_root
