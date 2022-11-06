# -> {"WordExpired":"word"}
# {"WordRemoved":"word"} ->
import json

def remove_word(data:str): # Example of how to read json str in lobby.py
    """
    Read JSON WordExpired and return WordRemoved
    """
    data['WordRemoved'] = data["word"]
    del data["word"]
    return data

if __name__ == "__main__":
    data = {"word": ["stable", "tgp", "complex", "professionals", "advocate"]}
    remove_word(data)
    print(data)
