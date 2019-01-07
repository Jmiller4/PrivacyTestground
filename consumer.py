# holds description of a "consumer" class/object

import random
import numpy as np
import math
from entity import *
from federation import *


class Consumer(Entity):

    def __init__(self, fed):
        Entity.__init__(self, fed)
        self.data = dict()
        self.data_simple = self.generate_data_simple()

        self.data_hash = hash(str(self.data_simple))
        self.fed.add_to_blockchain({"type": "consumer join", "id": self.id, "info hash": self.data_hash})

    # def generateData(self):
    #     #Location is uniformly distributed over earth
    #     latitude = random.uniform(-90, 90)
    #     longitude = random.uniform(-180, 180)
    #
    #     #Political ideology sepctrum is normally distributed
    #     ideology = random.gauss(0, 10)
    #
    #     #Number of friends is based on a possion distribution for the 100s and 10s place and uniformly distributed in ones place
    #     numFriends = math.ceil(np.random.poisson(2) * 100 + np.random.poisson(4) * 10 + random.uniform(0, 9))
    #
    #     #Binary-gendered individuals created with even distribution male and female
    #     isMale = 1 * (random.random() > .5)
    #
    #     self.data["lat"] = latitude
    #     self.data['long'] = longitude
    #     self.data['ideology'] = ideology
    #     self.data['Friends'] = numFriends
    #     self.data['isMale'] = isMale

    def generate_data_simple(self):
        return [random.randint(0, 10) for _ in range(5)]

    # def updateData(self, key, value):
    #     self.data[key] = value

    # distort should be in the federation class
    # def Distort(self, alpha):
    #     Distort = dict()
    #     for key in self.data:
    #         #Degree of variability should be based on underlying true distribution
    #         #Limit to a minimum number of users to preserve identity and provide distribution
    #         rndSeed = random.random()
    #         neg = random.random() > .5
    #         if neg :
    #             rndSeed = -1 * rndSeed
    #         Distort[key] = self.data[key] + alpha * rndSeed
    #     return Distort

    def exchange(self, v, t):
        if v.accept_exchange(self.id):
            # "bargain" over alpha
            alpha = Federation.alpha_bargain(self, v)
            # distort data according to alpha
            d = Federation.distort(self.data_simple, alpha, 1)
            rec = v.send_info(d, self, t)
            self.fed.add_to_blockchain_buffer({"type": "transaction", "time": t, "consumer": self.id, "vendor": v.id, "alpha hash": hash(alpha), "distorted data hash": hash(str(d)), "recommendation hash": hash(rec)})

    def getData(self, alpha):
        return self.Distort(alpha)

    def toString(self):
        dictString = "User: " + str(self.id) + '\n'
        for x in self.data:
            dictString = dictString + x + ': ' + str(self.data[x]) + '\n'
        return(dictString)


