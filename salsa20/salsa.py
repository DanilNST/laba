with open("encrypted.txt") as file:
    input_text = [bytearray.fromhex(line) for line in file.readlines()]

input_key = bytearray.fromhex("the pangs of dispriz'd love, the law's delay,".encode('utf-8').hex())
key = [a ^ b for a, b in zip(input_text[2], input_key)]

with open("decrypted.txt", "a") as file:
    decrypted = [''.join([chr(a ^ b) for a, b in zip(key, line)]) for line in input_text]
    print(decrypted)
