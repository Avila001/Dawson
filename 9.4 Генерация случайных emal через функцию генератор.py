import random
from string import ascii_lowercase, ascii_uppercase


chars = ascii_lowercase + ascii_uppercase
random.seed(1)


def gen_mail(N):
    while True:
        passw = ''
        for i in range(N):
            passw += chars[random.randint(0, len(chars)-1)]
        passw += '@mail.ru'
        yield passw

N = 8
new_passw = gen_mail(N)
for i in range(5):
    print(next(new_passw))
