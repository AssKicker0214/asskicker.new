import os
import time
import random as rd
import string

control = {
    # token: expire_time
}

md5_password = None if not os.path.exists('passwd') else open('passwd', encoding='utf-8').readline()


def login_with_hashed_password(hashed: str) -> bool or str:
    if md5_password is None:
        print('passwd file not found')
        return False

    population = string.ascii_letters + string.digits

    def random_token(length=16):
        return ''.join([rd.choice(population) for _ in range(length)])

    if hashed == md5_password:
        # token expire in 24 hours
        expire_time = int(time.time()) + 24 * 3600
        token = random_token()
        while token in control:
            token = random_token()
        control[token] = expire_time
        return token
    else:
        return False


def check_login(token: str) -> bool:
    """
    `token` should be registered in `control`, AND not expired
    :param token:
    :return:
    """
    return token is not None and token in control and time.time() < control[token]
