import json

class objJson(object):
    def __init__(self, data):
        self.__dict__ = json.loads(json.dumps(data))