# holds description of a "consumer" class/object

import random
import numpy as np
import math

class consumer:

    def __init__(self):
        self.id = random.getrandbits(128)
        self.data = dict()
        self.alpha = random.uniform(0, 1)

    def generateData(self):
        #Location is uniformly distributed over earth
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)

        #Political ideology sepctrum is normally distributed
        ideology = random.gauss(0, 10)

        #Number of friends is based on a possion distribution for the 100s and 10s place and uniformly distributed in ones place
        numFriends = math.ceil(np.random.poisson(2) * 100 + np.random.poisson(4) * 10 + random.uniform(0, 9))

        #Binary-gendered individuals created with even distribution male and female
        isMale = 1 * (random.random() > .5)

        self.data["lat"] = latitude
        self.data['long'] = longitude
        self.data['ideology'] = ideology
        self.data['Friends'] = numFriends
        self.data['isMale'] = isMale

    def updateData(self, key, value):
        self.data[key] = value

    def toString(self):
        dictString = "User: " + str(self.id) + '\n'
        for x in self.data:
            dictString = dictString + x + ': ' + str(self.data[x]) + '\n'
        return(dictString)