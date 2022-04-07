import csv
import random
import hashlib
import bcrypt
from string import ascii_letters, digits


def generate(num, top_100, top_10M):
    passwords = []
    for _ in range(num):
        r = random.randint(1, 100)
        if r <= 10:
            passwords.append(random.choice(top_100))
        elif r <= 95:
            passwords.append(random.choice(top_10M))
        else:
            password_symbols = ascii_letters + digits
            passwords.append(''.join(random.choices(password_symbols, k=random.randint(8, 16))))
    return passwords


def pass_md5(password):
    return hashlib.md5(bytes(password, encoding='ascii')).hexdigest()


def pass_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes(password, encoding='ascii'), salt).decode()
    return salt, hashed


def main():
    with open('100-passwords.txt') as file:
        top_100 = [password.strip() for password in file.readlines()]

    with open('10m-passwords.txt') as file:
        top_10m = [password.strip() for password in file.readlines()]

    passwords = generate(100, top_100, top_10m)
    with open('100k.txt', 'w') as file:
        for password in passwords:
            file.write(pass_md5(password))
            file.write('\n')

    with open('10k_hash.csv', 'w') as csv_file:
        csv_table = csv.writer(csv_file)
        csv_table.writerow(['hash', 'salt'])
        for password in passwords:
            salt, hashed = pass_bcrypt(password)
            csv_table.writerow([hashed, salt.decode()])


if __name__ == '__main__':
    main()
