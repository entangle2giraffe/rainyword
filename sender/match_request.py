import time
match_request = []

# add matching request from a client to match_request
def add_request(sender_id, receiver_id):
    match_request.append({"sender":sender_id, "receiver":receiver_id})


# remove matching request with specific id from match_request
def remove_request(id):
    i = 0
    while i < len(match_request):
        if match_request[i]["sender"] == id or match_request[i]["receiver"]== id:
            match_request.pop(i)
            i = i-1
        if i == len(match_request)-1:
            break
        i = i+1

""" 
def check():
    while True:
        check_request()
        time.sleep(1)
"""

# check for matched request and return matched id pair
def check_request():
    for i in range(len(match_request)):
        id1 =  match_request[i]["sender"]
        id2 = match_request[i]["receiver"]
        for i in range(len(match_request)):
            if id2 ==  match_request[i]["sender"] and id1 == match_request[i]["receiver"]:
                remove_request(id1)
                remove_request(id2)
                return [id1,id2]
    return 0

#def match_start():

if __name__ == "__main__":
    add_request(123,1)
    print(match_request)
    add_request(122,22)
    add_request(13,15)
    add_request(1,123)
    print(match_request)
    print(check_request())
    print(match_request)
