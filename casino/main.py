from casino.const import URL
from player import Player
from MT19937 import MT19937
import datetime as dt


def lcg_crack(player: Player):
    M = (2 ** 32) // 2
    n1 = player.play('Lcg', 1, 1)['realNumber']
    n2 = player.play('Lcg', 1, 1)['realNumber']
    n3 = player.play('Lcg', 1, 1)['realNumber']

    a = ((n3 - n2) * pow((n2 - n1), -1, M)) % M
    b = (n2 - n1 * a) % M
    print(f'A={a}, B={b}')

    value = player.play('Lcg', 1, 1)['realNumber']
    num = (a * value + b) % M

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
    player = Player(URL)
    lcg_crack(player)
    player = Player(URL)
    mt_crack(player)


if __name__ == '__main__':
    main()
