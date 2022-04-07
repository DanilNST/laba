from random import randint, choice
from string import ascii_letters, digits
import hashlib
import bcrypt


def get100():
    passwords = []
    with open('100_passwords.txt') as file:
        for p in file.readlines():
            p = p.strip()
            passwords.append(p)
    return passwords


def get1M():
    passwords = []
    with open('10m-passwords.txt') as file:
        for p in file.readlines():
            p = p.strip()
            passwords.append(p)
    return passwords




def generate(num, top_100, top_1M):
    passwords = []
    for _ in range(num):
        r = randint(1, 100)
        if r in range(1, 10):
            passwords.append(choice(top_100))
        elif r in range(11, 95):
            passwords.append(choice(top_1M))
        else:
            passwords.append(''.join([choice(ascii_letters+digits) for _ in range(randint(8, 16))]))
    return passwords


def pass_md5(password):
    return hashlib.md5(bytes(password, encoding="ascii")).hexdigest()


def pass_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(password, encoding="ascii"), salt).decode()
    print(hashed)
    return salt, hashed


top_100 = get100()
top_1M = get1M()
passes = generate(100, top_100, top_1M)
print(passes)

file = open('100k.txt', 'w')
for p in passes:
    file.write(pass_md5(p))
    file.write('\n')
file.close()
