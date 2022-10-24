import json
import random
with open("words_list.json") as f:
    content = json.loads(f.read())
words = random.sample(content,5)