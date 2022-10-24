from Object import Player
from utils import class_to_json
import json

def json_players(p1, p2):
    # Player Json
    p1j,p2j = class_to_json(p1),class_to_json(p2)

    data = {
        "Player":{
            "player1": p1j,
            "player2": p2j
        }
    }

    return json.dumps(data)

if __name__ == "__main__":
    p1,p2 = Player(1),Player(2)
    x = player(p1,p2)
    print(json.loads(x))