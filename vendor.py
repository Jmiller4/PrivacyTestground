# holds decription of a "vendor" object/class

from entity import *
from consumer import *
from globaldata import *


class Vendor(Entity):
    def __init__(self, fed):
        Entity.__init__(self, fed)
        self.consumersIKnowAbout = list()
        self.model = self.generate_model()
        self.model_hash = hash(str(self.model))
        self.fed.addMember(self, self.id, self.model_hash)

        self.consumerOfAgreementInProgress = None

        self.memory = list()

    # def model_as_algorithm(self, data):
    #     gender = data["isMale"] == 1
    #     neutral = data["ideology"] > -1 and data["ideology"] < 1
    #     popular = data["Friends"] > 300
    #     ans = gender + neutral + popular >= 2
    #     return ans

    @staticmethod
    def generate_model():
        # the "model" is a list of (int, movie) tuples
        # if a consumer's data is a list of 5 floats between 0 and 1, the sum of all data could be between 0 and 5
        m = list()
        current_threshhold = 0
        while current_threshhold < 50:
            m.append((current_threshhold, random.choice(movieList)))
            current_threshhold += random.randint(5, 15)
        return m

    def get_model(self):
        return self.model

    def accept_exchange(self, c):
        if type(self.fed.entities[c.consumerID]) == consumer.Consumer:
            self.consumerOfAgreementInProgress = c
            return True
        else:
            return False

    def recieve_info(self, d):
        alpha = Federation.alpha_bargain(self, self.consumerOfAgreementInProgress)
        rec = Federation.recommend(self.model, d)
        self.fed.add_to_blockchain_buffer(
            {"type": "transaction", "time": self.time, "consumer": self.consumerOfAgreementInProgress.id, "vendor": self.id, "alpha hash": hash(alpha),
             "distorted data hash": hash(str(d)), "recommendation hash": hash(rec)})
        self.memory.append({"time": self.time, "consumer": self.consumerOfAgreementInProgress.id, "alpha": alpha,
             "distorted data": d, "recommendation": rec})
        self.consumerOfAgreementInProgress.recieve_rec(rec)
        self.consumerOfAgreementInProgress = None

    def updateKnowledgeOfOtherParties(self):
        self.consumersIKnowAbout = self.fed.consumerList