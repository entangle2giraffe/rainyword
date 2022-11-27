# {"ID":1, "playerTyped":"word"}
import json
from utils import json_read, jsonify, save_to_file
from Object import Player
import json
# {"scoreList":[{"id":0,"score":100},{"id":3,"score":99}]}

def add_point(data:str): # Example of how to read json str in lobby.py
    """Add Point to the Player class instance using Object.py and
    return json above"""
    data = json.loads(data)
    return data

def read_word(data:str):
    """Remove the word player typed from dict"""
    #remove_word.py function here
    pass

if __name__ == "__main__":
    data = '{"ID":1,"playerTyped":"apple"}'
    add_point(data)
    # add_point(data)
    # remove_word(data) from expired_word.py
