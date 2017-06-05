import string
from random import *

def gen_password(size=8):
    characters = string.ascii_letters + string.digits
    return "".join(choice(characters) for _ in range(size))


if __name__ == '__main__':
    print(gen_password(20))
