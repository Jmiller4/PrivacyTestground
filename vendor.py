# holds decription of a "vendor" object/class

import random


class vendor:
    def __init__(self):
        self.id = random.getrandbits(128)

    def model(self, data):
        gender = data["isMale"] == 1
        neutral = data["ideology"] > -1 and data["ideology"] < 1
        popular = data["Friends"] > 300
        ans = gender + neutral + popular >= 2
        return ans
