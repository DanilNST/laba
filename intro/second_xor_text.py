import binascii


def main():
    dictionary = str.maketrans({'\x00': ' ', '\x0e': '\n', 'Â': '', '': '', '½': "'", '¼': "'"})

    with open('sources/xor_secret.txt', 'r') as f:
        data_lines = f.readlines()[0:1]

    for data_line in data_lines:
        data_line = data_line.strip()
        data_line = binascii.unhexlify(data_line)
        new_data = ''
        for byte in data_line:
            new_data += chr(byte ^ 23)
        print(new_data.translate(dictionary))


if __name__ == '__main__':
    main()
