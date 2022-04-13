import random
import string
from math import log10
from random import sample


class Gene:
    def __init__(self, data):
        self.data = data
        self.score = 0

    def crossover(self, partner):
        child_data = []
        array = set(self.data)

        for own_data, partner_data in zip(self.data, partner.data):
            new_char = (
                random.choice((own_data, partner_data))
                if own_data in array and partner_data in array
                else (own_data if own_data in array else partner_data)
            )

            child_data.append(new_char)
            array.discard(new_char)

        child = Gene(''.join(child_data))
        return child

    def mutation(self):
        ch2: int
        ch1: int
        ch1, ch2 = sample(range(len(self.data)), 2)
        data_array = list(self.data)
        data_array[ch1], data_array[ch2] = data_array[ch2], data_array[ch1]
        self.data = ''.join(data_array)

    def get_score(self, text, dictionary, miss):
        text = text.translate(str.maketrans(string.ascii_uppercase, self.data))
        bit_length = len(list(dictionary.keys())[0])
        bits = len(text) - bit_length
        self.score = -sum(dictionary.get(text[i : i + bit_length], miss) for i in range(bits)) / bits


def main():
    with open('sources/ngragms.txt') as file:
        lines = file.readlines()

    with open('sources/xor_secret.txt') as file:
        substitution = file.readlines()[2]

    ngr4 = dict(tuple(line.split(maxsplit=1)) for line in lines)  # noqa
    s = sum(map(int, ngr4.values()))
    new_ngr4 = {k: int(v) / s for k, v in ngr4.items()}
    miss = log10(0.01 / s)

    genes = [Gene(''.join(random.choice(string.ascii_uppercase) for _ in range(26))) for _ in range(10000)]

    for gen in genes:
        gen.get_score(substitution, new_ngr4, miss)

    best_gen = genes[0]

    for i in range(128):
        genes = sorted(genes, key=lambda x: x.score)[:200]
        best_gen = genes[0]
        print(f'Generation {i} started, best gene data={best_gen.data}')

        for _ in range(1000 - len(genes)):
            p1, p2 = sample(range(len(genes)), 2)
            genes.append(genes[p1].crossover(genes[p2]))

        for gene in genes:
            gene.mutation()
            gene.get_score(substitution, new_ngr4, miss)

    res4 = substitution.translate(str.maketrans(string.ascii_uppercase, best_gen.data))
    print(res4)


if __name__ == '__main__':
    main()
