import json
import os

def plaintext_to_list(filename):
    words_list = []

    with open(filename) as f:
        lines = f.readlines()
        
        for line in lines:
            words_list.append(line.strip())

    return words_list

def jsonify(ll):
    res = json.dumps(ll)
    return res

def save_to_file(filename, jsonObj):
    with open(filename, 'a') as f:
        f.write(jsonObj)

def class_to_json(cl):
    """Convert class to json format"""
    json_str = json.dumps(
        {"id": cl.ID,"point": cl.point}
    )
    return json_str

def json_read(res):
    """Read JSON in plaintext"""
    return json.loads(res)

def json_modify(filename:str, key:str, value):
    with open(filename, 'r') as f:
        data = json.load(f)  
    data[key] = value

    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    #pl = plaintext_to_list('wordlist.10000')
    #x = {
    #    "categories": {
    #    "MIT 10000 words":  pl
    #    }
    #}
    #jsonObj = jsonify(x)
    #save_to_file('words_list.json', jsonObj)
    pass

if __name__ == "utils":
    import json