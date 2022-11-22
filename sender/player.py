import sys
import json
import os

# import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Object import Player
player_list = []
dict = {}


def assign_id(n:int):
    data ={
        "assignID":n
    }
    return json.dumps(data)

def send_player_list():
    #return json.dumps(player_list)
    return json.dumps(dict)

#add a client to the player_list
def add_to_list(n:int, name, isBusy):
    player_list.append({"id":n, "name":name, "isBusy":isBusy})
    dict["playerList"] = player_list

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

