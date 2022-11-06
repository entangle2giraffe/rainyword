import sys
import json
import os

# import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Object import Player

def assign_id(n:int):
    data ={
        "assignID":n
    }
    return json.dumps(data)


def json_players(p1, p2):
    # Player Json
    data = {
        "player":[p1.point, p2.point]
    }

    return json.dumps(data)

if __name__ == "__main__":
    p1,p2 = Player(1),Player(2)
    x = json_players(p1,p2)
    print(x)
