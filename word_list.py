import json
import random
import time
from threading import Timer

def generate_random_words() -> list:
    """
    Comment here <--
    """
    with open("words_list.json") as f:
        content = json.loads(f.read())
        content = content['categories']['MIT 10000 words']
        words = random.sample(content, 5)
    return words

# [TODO] Send words list for 5 min with delay between each
def ThaksinDelay():
    t = Timer(10, generate_random_words)
    t.start()
    t.join()

if __name__ == "__main__":
    print(ThaksinDelay())
