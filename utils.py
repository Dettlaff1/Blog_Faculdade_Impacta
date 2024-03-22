import json

def load_posts():
    with open('data.json', 'r') as file:
        posts = json.load(file)
    return posts