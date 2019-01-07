# holds decription of a "vendor" object/class

from entity import *
from consumer import *
from globaldata import *


class Vendor(Entity):
    def __init__(self, fed):
        Entity.__init__(self, fed)
        self.model = self.generate_model()
        self.model_hash = hash(str(self.model))
        self.fed.add_to_blockchain({"type": "vendor join", "id": self.id, "model hash": self.model_hash})

    # def model_as_algorithm(self, data):
    #     gender = data["isMale"] == 1
    #     neutral = data["ideology"] > -1 and data["ideology"] < 1
    #     popular = data["Friends"] > 300
    #     ans = gender + neutral + popular >= 2
    #     return ans

    def generate_model(self):
        # the "model" is a list of (int, movie) tuples
        # if a consumer's data is a list of 5 floats between 0 and 1, the sum of all data could be between 0 and 5
        m = list()
        currentThreshhold = 0
        while currentThreshhold < 50:
            m.append((currentThreshhold, random.choice(movieList)))
            currentThreshhold += random.randint(5, 15)
        return m

    def get_model(self):
        return self.model

    def accept_exchange(self, consumerID):
        if type(self.fed.entities[consumerID]) == Consumer:
            return True
        else:
            return False

    def send_info(self, d, c, t):
        alpha = Federation.alpha_bargain(self, c)
        rec = Federation.recommend(self.model, d)
        self.fed.add_to_blockchain_buffer(
            {"type": "transaction", "time": t, "consumer": c.id, "vendor": self.id, "alpha hash": hash(alpha),
             "distorted data hash": hash(str(d)), "recommendation hash": hash(rec)})
        return rec
