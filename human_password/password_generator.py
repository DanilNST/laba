#!/usr/bin/env python
import argparse
import csv
import random
import hashlib
from typing import TextIO, Tuple

import bcrypt
from string import ascii_letters, digits


def generate(num, top_100, top_10m):
    passwords = []
    for _ in range(num):
        r = random.randint(1, 100)
        if r <= 10:
            a = random.choice(top_100)
            passwords.append(a)
        elif r <= 95:
            passwords.append(random.choice(top_10m))
        else:
            password_symbols = ascii_letters + digits
            passwords.append(''.join(random.choices(password_symbols, k=random.randint(8, 16))))
    return passwords


def pass_md5(password: str) -> Tuple[str]:
    return hashlib.md5(bytes(password, encoding='ascii')).hexdigest(),


def pass_bcrypt(password: str) -> Tuple[str, str]:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(password, encoding='ascii'), salt).decode()
    return hashed, salt.decode()


def sha_1(password: str) -> Tuple[str, str]:
    salt = bcrypt.gensalt().decode()
    return hashlib.sha1(bytes(password+salt, encoding='ascii')).hexdigest(), salt


def main(num: int, top_100: TextIO, top_10m: TextIO, output: TextIO, algorithm: str, with_header: bool):
    algorithms = {'md5': pass_md5, 'bcrypt': pass_bcrypt, 'sha-1': sha_1}

    top_100_passwords = [password.strip() for password in top_100.readlines()]
    top_10m_passwords = [password.strip() for password in top_10m.readlines()]

    passwords = generate(num, top_100_passwords, top_10m_passwords)

    csv_table = csv.writer(output, delimiter='.')
    if with_header:
        if algorithm in ['sha-1', 'bcrypt']:
            csv_table.writerow(['hash', 'salt'])
        else:
            csv_table.writerow(['hash'])

    for password in passwords:
        csv_table.writerow(algorithms[algorithm](password))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num', type=int, default=100)
    parser.add_argument('-t', '--top_100', type=argparse.FileType('r'), default=open('100-passwords.txt'))
    parser.add_argument('-m', '--top_10M', type=argparse.FileType('r'), default=open('10m-passwords.txt'))
    parser.add_argument('-o', '--output', type=argparse.FileType('w'))
    parser.add_argument('-a', '--algorithm', choices=['md5', 'sha-1', 'bcrypt'], default='md5')
    parser.add_argument('--with-header', action='store_true', default=False)
    _args = parser.parse_args()
    main(_args.num, _args.top_100, _args.top_10M, _args.output, _args.algorithm, _args.with_header)
