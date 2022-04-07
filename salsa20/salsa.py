import argparse
import sys
from typing import TextIO


def main(source: TextIO, dest: TextIO, key: bytearray):
    input_text = [bytearray.fromhex(line) for line in source.readlines()]
    source_key = [a ^ b for a, b in zip(input_text[2], key)]
    decrypted = ''.join([''.join([chr(a ^ b) for a, b in zip(source_key, line)]) for line in input_text])
    dest.write(decrypted)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Salsa20')
    parser.add_argument('-s', '--source', type=argparse.FileType('r'), default=sys.stdin, help='Source file')
    parser.add_argument('-d', '--dest', type=argparse.FileType('w'), default=sys.stdout, help='Destination file')
    parser.add_argument(
        '-k',
        '--key',
        type=lambda f: bytearray(f.decode()),
        default=bytearray(b"the pangs of dispriz'd love, the law's delay,"),
        help='key',
    )
    _args = parser.parse_args()
    main(_args.source, _args.dest, _args.key)
