import requests

ARCHIVES = "https://api.chess.com/pub/player/falc0nfeast/games/archives"

all_archieves = requests.get(ARCHIVES).json()

for i in all_archieves['archives']:
    r = requests.get(i).json()

    with open('chess.com.pgn', 'a') as f:
        for g in r['games']:
            f.write(g['pgn'])
            f.write("\n\n")
