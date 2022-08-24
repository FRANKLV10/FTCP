import json


def get_config(path):
    with open(path, encoding="utf8") as file:
        data = file.read()
        config = json.loads(data)
        return config
