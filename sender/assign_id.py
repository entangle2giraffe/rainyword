# [CLIENT] CONNECTED TO SERVER
# [SENDER] {"assignID":id}
import json

def return_id(n:int):
    data ={
        "assignID":n
    }
    return json.dumps(data)

if __name__ == "__main__":
    print(return_id(2))
