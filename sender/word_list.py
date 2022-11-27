import json
import random
import time, os, sys
import threading

# import from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from utils import jsonify

# return json of words ex. {"word": ["adopt", "blacks", "personals", "coat", "guided"]}
def generate_random_words(n:int) -> list:
    """
    Generate the random word from the list
    """
    with open("words_list.json") as f:
        content = json.loads(f.read())
        content = content['categories']['MIT 10000 words']
        words = jsonify({"words":random.sample(content, n)})  
        return words

# [TODO] Send words list for 5 min with delay between each
def countdown():
    #countdown code
    global my_timer
    my_timer = 5 * 60
    for x in range(300):
        my_timer = my_timer-1
        time.sleep(1)

def delay():
    #delay for 3 sec
    countdown_thread = threading.Thread(target=countdown)
    countdown_thread.start()
    while my_timer > 0:
        generate_random_words()
        time.sleep(3)


if __name__ == "__main__":
    delay()
