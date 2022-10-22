import json

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
    json_str = json.dumps(cl.__dict__)
    return json_str


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