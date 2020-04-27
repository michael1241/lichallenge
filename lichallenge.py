#! /usr/bin/env python3

import requests
import time


url = 'https://lichess.dev/api/challenge/open'
clock = int(input("Clock time in seconds:"))
inc = int(input("Clock increment in seconds:"))
games = int(input("How many open challenges to create:"))
variant = input("Variant (blank for standard):")
fen = input("Starting FEN (blank for default):")

if not fen:
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
if not variant:
    variant = 'standard'

gamelinks = []

for n in range(games):
    payload = {'clock.limit': clock, 'clock.increment': inc, 'variant': variant, 'fen': fen}
    r = requests.post(url, data=payload)
    gamelinks.append(r.json()['challenge']['url'])
    time.sleep(1)

for game in gamelinks:
    print(game)
