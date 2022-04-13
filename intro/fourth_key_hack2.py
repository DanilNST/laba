import base64
import string
from functools import reduce
from math import gcd


fault = 2
shift_multiplier = 3
SYMBOLS = string.ascii_letters + ',. '


def find_key_length(encrypted):
    good_shifts = []
    MA = 5
    SUM = 0
    encrypted = base64.b64decode(encrypted)

    for shift in range(1, 51):
        count = sum([a == b for a, b in zip(encrypted, encrypted[shift:] + encrypted[:shift])])
        if count > MA * shift_multiplier:
            good_shifts.append(shift)
        SUM += count
        MA = SUM / shift
    best_shift = reduce(gcd, good_shifts)
    return best_shift


def vigenere_xor(text, key):
    key_length = len(key)
    text = base64.b64decode(text)
    key = [ord(character) for character in key]
    result = ''.join(chr(text[i] ^ key[i % key_length]) for i in range(len(text)))
    return result


def xor_key_hack(encrypted):
    key = 'L0l'

    key_length = find_key_length(encrypted)
    items = [encrypted[x : x + 12] for x in range(0, len(encrypted), 12)]

    possible_keys = []
    for n in range(0, key_length):
        temp = ''.join([items[i][n] for i in range(0, len(items) - 1)])
        local_possible_keys = []
        local_max = 0
        for i in range(2 ** 8 - 1):
            count = sum(chr(ord(item) ^ i) in SYMBOLS for item in temp)
            local_max = max(count, local_max)

        for i in range(2 ** 8 - 1):
            count = sum(chr(ord(item) ^ i) in SYMBOLS for item in temp)
            if count >= local_max - fault:
                local_possible_keys.append(chr(i))

        possible_keys.append(local_possible_keys)

    return vigenere_xor(encrypted, key)


def main():
    with open('sources/xor_secret.txt', 'r') as f:
        data = f.readlines()[1]
    print(xor_key_hack(data))


if __name__ == '__main__':
    main()
