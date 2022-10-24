import json
import random

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
def passholder():
    pass

if __name__ == "__main__":
    print(generate_random_words())