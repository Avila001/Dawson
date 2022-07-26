from re import I
from string import ascii_lowercase, ascii_uppercase
import random

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

random.seed(1)
def gen_password(N):
    while True:
        new_pass = ''
        for i in range(N):
            new_pass += chars[random.randint(0, len(chars) - 1)]
        yield new_pass


N = 8
password = gen_password(N)
for i in range(N):
    print(next(password))
