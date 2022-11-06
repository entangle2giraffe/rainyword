import json
import time
import sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import sender.player as player
from utils import json_modify

class Lobby:
    ps1 = 0
    ps2 = 0

    def __init__(self, filename:str):
        self.filename = filename # file where the status will be saved

    def read_status(self, data:str) -> None:
        """Read status of json string if both
        of them are ready (1) then update the file"""
        data = json.loads(data)['status']
        player_id = str(data[0])
        status = data[1]
        if player_id == 1:
            self.ps1 = status
        elif player_id == 2:
            self.ps2 = status
        json_modify(self.filename, player_id, status)

    def _return_dict(self) -> dict:
        """Debugging purpose only"""
        return {"1":self.ps1, "2":self.ps2}

    def reset_dict(self) -> None:
        """Reset back the file after the game end"""
        json_modify(self.filename, "1", 0)
        json_modify(self.filename, "2", 0)
        

if __name__ == "__main__":
    lb = Lobby("status.json")
    data1 = '{"status": [1,1]}'
    lb.read_status(data1)
    time.sleep(1)
    print(lb._return_dict())
    data2 = '{"status": [2,0]}'
    lb.read_status(data2)
    time.sleep(1)
    print(lb._return_dict())
    data2 = '{"status": [2,1]}'
    lb.read_status(data2)
    time.sleep(1)
    print(lb._return_dict())
    lb.reset_dict()
