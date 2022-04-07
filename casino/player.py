from datetime import timedelta, datetime
from urllib.parse import urljoin
from dateutil.parser import isoparse

import requests


class Player:
    def __init__(self, unique_id: int, base_url: str):
        self.base_url: str = base_url
        self.unique_id: int = unique_id
        url = urljoin(self.base_url, 'createacc')

        response = requests.get(url, params={'id': self.unique_id})
        response.raise_for_status()

        self.money: int = response.json()['money']
        self.deletion_time: datetime = isoparse(response.json()['deletionTime'])
        self.creation_time: datetime = self.deletion_time - timedelta(hours=1)

    def play(self, game_mode, bet, number):
        url = urljoin(self.base_url, 'play{}'.format(game_mode))
        response = requests.get(url, params={'id': self.unique_id, 'bet': bet, 'number': number})
        if response.ok:
            self.money = response.json()['account']['money']
            return response.json()
