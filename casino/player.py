import random
from datetime import timedelta, datetime
from typing import Optional
from urllib.parse import urljoin
from dateutil.parser import isoparse

import requests


class Player:
    def __init__(self, base_url: str):
        self.base_url: str = base_url
        url = urljoin(self.base_url, 'createacc')
        self.unique_id: Optional[int] = None
        while self.unique_id is None:
            unique_id = random.randint(1, 100000)
            response = requests.get(url, params={'id': self.unique_id})
            if response.ok:
                self.unique_id = unique_id
                self.money: int = response.json()['money']
                self.deletion_time: datetime = isoparse(response.json()['deletionTime'])
                self.creation_time: datetime = self.deletion_time - timedelta(hours=1)
                break

    def play(self, game_mode, bet, number):
        url = urljoin(self.base_url, 'play{}'.format(game_mode))
        response = requests.get(url, params={'id': self.unique_id, 'bet': bet, 'number': number})
        if response.ok:
            self.money = response.json()['account']['money']
            return response.json()
