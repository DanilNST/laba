import base64


def main():
    with open('sources/binary.txt') as f:
        data = f.read()

    string = ''
    for byte_num in range(len(data) // 8):
        byte = data[byte_num * 8:(byte_num + 1) * 8]
        byte_int = int(byte, 2)
        string += chr(byte_int)

    print(base64.b64decode(string).decode())


if __name__ == '__main__':
    main()
