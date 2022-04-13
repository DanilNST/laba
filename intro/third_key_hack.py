import base64
import string

SYMBOLS = string.ascii_letters + ',. '


def main():
    with open('sources/xor_secret.txt', 'r') as f:
        encrypted = f.readlines()[1].strip()
    fault = 2
    encrypted = base64.b64decode(encrypted)
    possible_keys = []

    local_max = 0
    for i in range(2 ** 8 - 1):
        count = sum(chr(item ^ i) in SYMBOLS for item in encrypted)
        local_max = max(count, local_max)

    for i in range(2 ** 8 - 1):
        count = sum(chr(item ^ i) in SYMBOLS for item in encrypted)
        if count >= local_max - fault:
            possible_keys.append(chr(i))

    print('possible keys:', ','.join(possible_keys))


if __name__ == '__main__':
    main()
