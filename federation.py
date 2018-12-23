# holds description of a "federation" class/object

import random

class federation:

    def __init__(self):
        self.consumerList = list()
        self.vendorList = list()
        self.blockchain = list()


    def distort(self, info, alpha):

        # if info is a list of numbers and alpha is a number between 0 and 1,
        # then distort will sum each number of the list with a random number between -alpha and alpha,
        # and return the new list created by that process

        d = list()

        for i in info:
            d.append(i + random.uniform(-alpha, alpha))

        return d


    def reccomend(self, model, distortedInfo):

        # here's my first shot at a simple way to do models and recommendations:
        # model is a list of (number, string) tuples
        # the recommendation rule is: the consumer's distorted info (a list of numbers) is summed up
        # the consumer is recommended the product that corresponds to the highest number that their sum exceeds in model
        # so if the vendor's model is [(0, "applebees"), (2, "red lobster"), (5, "ruth's chris")]
        # then consumers with a sum between 0 and 2 will be recommended applebees, consumers with a sum between 2 and 5
        # will be recommended red lobster, and consumers with a sum of 5 and up will be recommended ruth's chris
        # (which is a fancy restaurant, just to be clear about that).
        # For now, let's also assume that the numbers in the model will be in increasing order

        s = sum(distortedInfo)

        rec = "None"

        for x in model:
            if s > x[0]:
                rec = x[1]

        return rec



    def addToBlockchain(self, data):

        self.blockchain.append(data)
        self.broadcastBlockchain()

    def broadcastBlockchain(self):

        for c in self.consumerList:
            c.updateBlockchain(self.blockchain)

        for v in self.vendorList:
            v.updateBlockchain(self.blockchain)