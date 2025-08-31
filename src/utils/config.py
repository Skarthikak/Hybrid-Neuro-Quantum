import json, os

def load_config(path):
    if not os.path.exists(path):
        raise FileNotFoundError("Config not found: {}".format(path))
    with open(path) as f:
        return json.load(f)
