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

    def Distort(self, alpha):
        Distort = dict()
        for key in self.data:
            #Degree of variability should be based on underlying true distribution
            #Limit to a minimum number of users to preserve identity and provide distribution
            rndSeed = random.random()
            neg = random.random() > .5
            if neg :
                rndSeed = -1 * rndSeed
            Distort[key] = self.data[key] + alpha * rndSeed
        return Distort

    def getData(self, alpha):
        return self.Distort(alpha)

    def getID(self):
        return self.id

    def toString(self):
        dictString = "User: " + str(self.id) + '\n'
        for x in self.data:
            dictString = dictString + x + ': ' + str(self.data[x]) + '\n'
        return(dictString)
