from http import client
from utils import json_read, jsonify, save_to_file
import player

def read_status(data:str) -> bool:
    """Read status of json string if both
    of them are ready (1) then return true"""
    data = jsonify(data)
    if data['Status']['player1']['ready'] == 1 and data['Status']['player2']['ready'] == 1:
        return True
    else: return False

def return_player(res:bool) -> None:
    """"If read_status() == True then return json_player from playr.py"""
    if res == True:
        return player.json_players(data['Status']['player1'],data['Status']['player2'])

if __name__ == "__main__":
    data = {'Status': {'player1': 1}, {'player2' : 2}}
    #res = read_status(data)
    #return_player(res)
    print(type(data))