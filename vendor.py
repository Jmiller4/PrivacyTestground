# holds decription of a "vendor" object/class

import random


class vendor:
    def __init__(self):
        self.id = random.getrandbits(128)
        self.recommend = self.model

    def model(self, data):
        gender = data["isMale"] == 1
        neutral = data["ideology"] > -1 and data["ideology"] < 1
        popular = data["Friends"] > 300
        ans = gender + neutral + popular >= 2
        return ans

    def getModel(self):
        return self.recommend

    def getID(self):
        return self.id
