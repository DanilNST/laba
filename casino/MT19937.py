# imported from https://github.com/yinengy/Mersenne-Twister-in-Python/blob/master/MT19937.py
# coefficients for MT19937
from casino.const import LOWER_MASK, UPPER_MASK

(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 0x6C078965


class MT19937:
    def __init__(self, seed=None):
        self.MT = [0] * n
        self.index = n
        if seed is not None:
            self.mt_seed(seed)

    def mt_seed(self, seed):
        self.MT[0] = seed
        for i in range(1, n):
            self.MT[i] = self.to_size(f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (w - 2))) + i, bits=32)

    def extract_number(self):
        if self.index >= 624:
            self.twist()

        y = self.MT[self.index]
        y ^= y >> u
        y ^= (y << s) & b
        y ^= (y << t) & c
        y ^= y >> l

        self.index += 1
        return self.to_size(y, bits=32)

    def twist(self):
        for i in range(n):
            x = self.to_size((self.MT[i] & UPPER_MASK) + (self.MT[(i + 1) % n] & LOWER_MASK), bits=32)
            self.MT[i] = self.MT[(i + m) % n] ^ (x >> 1)

            if x & 1 != 0:
                self.MT[i] ^= a

        self.index = 0

    @staticmethod
    def to_size(value, bits=32):
        return value & (2**bits - 1)


if __name__ == '__main__':
    generator = MT19937(123123123)
    for _ in range(n):
        print(generator.extract_number())
