import json
import random
import time
import threading

def generate_random_words() -> list:
    """
    Comment here <--
    random bullshit go
    """
    with open("words_list.json") as f:
        content = json.loads(f.read())
        content = content['categories']['MIT 10000 words']
        words = random.sample(content, 5)
        print(words)

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