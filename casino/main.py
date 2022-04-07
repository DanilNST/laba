import random

from casino.const import URL
from player import Player
from MT19937 import MT19937
import datetime as dt


M = (2 ** 32) // 2


def lcg_crack(player: Player):
    n1, n2, n3 = [player.play('Lcg', 1, 1)['realNumber'] for _ in range(3)]

    a = ((n3 - n2) * pow((n2 - n1), -1, M)) % M

    b = (n2 - n1 * a) % M
    print(f'A={a}, B={b}')

    val = player.play('Lcg', 1, 1)['realNumber']
    num = (a * val + b) % M

    while player.money <= 1000000:
        print(player.play('Lcg', player.money, num))
        num = (a * num + b) % M


def mt_crack(player):
    time_seed = player.creation_time - dt.datetime.fromtimestamp(0, dt.timezone.utc)

    generator = MT19937(int(time_seed.total_seconds()))
    while player.money <= 1000000:
        num = generator.extract_number()
        print(player.play('Mt', player.money, num))


def main():
    player = Player(random.randint(1, 10000), URL)
    lcg_crack(player)
    player = Player(random.randint(1, 10000), URL)
    mt_crack(player)


if __name__ == '__main__':
    main()
