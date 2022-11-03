# {"ID":1, "playerTyped":"word"}
import json
from utils import json_read, jsonify, save_to_file
from Object import Player
import json

p1,p2 = Player(1),Player(2)

def add_point(data:str): # Example of how to read json str in lobby.py
    """Add Point to the Player class instance using Object.py and
    return json above"""
    data = json.loads(data)
    if data["ID"] == 1:
        p1.add_point()
    if data["ID"] == 2:
        p2.add_point()
    return data

if __name__ == "__main__":
    data = '{"ID":1,"playerTyped":"apple"}'
    add_point(data)
    print(p1.__str__())
    # add_point(data)
    # remove_word(data) from expired_word.py
