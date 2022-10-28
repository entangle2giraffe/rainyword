from utils import json_read, jsonify, save_to_file
import player
from Object import Player
import json

def read_status(data:str) -> bool:
    """Read status of json string if both
    of them are ready (1) then return true"""
    data = json.loads(data)
    if data['Status'][0]['player'] == 1 and data['Status'][1]['player'] == 1:
        return True
    else: return False

def return_player(res:bool):
    """"If read_status() == True then return json_player from playr.py"""
    if res == True:
        p1 = Player(1)
        p2 = Player(2)
        data = player.json_players(p1,p2)
        print(data)

if __name__ == "__main__":
    data = '{"Status": [{"player":1},{"player":1}]}'
    return_player(read_status(data))
