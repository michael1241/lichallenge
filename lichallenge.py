#! /usr/bin/env python3

import requests
import time


url = 'https://lichess.dev/api/challenge/open'
clock = int(input("Clock time in seconds:"))
inc = int(input("Clock increment in seconds:"))
games = int(input("How many open challenges to create:"))

gamelinks = []

for n in range(games):
    payload = {'clock.limit': clock, 'clock.increment': inc}
    r = requests.post(url, data=payload)
    gamelinks.append(r.json()['challenge']['url'])
    time.sleep(1)

for game in gamelinks:
    print(game)
