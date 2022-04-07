import sys
from typing import TextIO


def main(source: TextIO, dest: TextIO, key: bytearray):
    input_text = [bytearray.fromhex(line) for line in source.readlines()]
    source_key = [a ^ b for a, b in zip(input_text[2], key)]
    decrypted = ''.join([''.join([chr(a ^ b) for a, b in zip(source_key, line)]) for line in input_text])
    dest.write(decrypted)


if __name__ == '__main__':
    main(open('encrypted.txt'), sys.stdout, bytearray(b"the pangs of dispriz'd love, the law's delay,"))
