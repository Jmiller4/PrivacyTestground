# holds description of a "federation" class/object

import random
import consumer
import vendor
import math

class Federation:

    def __init__(self):
        self.consumerList = list()
        self.vendorList = list()
        self.blockchain_buffer = set()
        self.blockchain = list()
        self.entities = dict()
        self.IDs = set()
        self.time = 0

    def addMember(self, e, id, firsthash):
        self.entities[id] = e
        self.IDs.add(id)
        if type(e) == consumer.Consumer:
            self.consumerList.append(e)
            self.add_to_blockchain({"type": "consumer join", "id": id, "info hash": firsthash})
        if type(e) == vendor.Vendor:
            self.vendorList.append(e)
            self.add_to_blockchain({"type": "vendor join", "id": id, "model hash": firsthash})
        # may want to add exception-throwing when this is called with an id that's already in use

    def add_to_blockchain_buffer(self, data):
        if str(data) in self.blockchain_buffer:
            self.blockchain.append(data)
            self.blockchain_buffer.remove(str(data))
        else:
            self.blockchain_buffer.add(str(data))

    def add_to_blockchain(self, data):
        self.blockchain.append(data)

    def blockchain_to_string(self):
        s = ""
        for entry in self.blockchain:
            s += str(entry) + "\n"
        return s

    @staticmethod
    def distort(info, alpha, seed):

        # if info is a list of numbers and alpha is a number between 0 and 1,
        # then distort will sum each number of the list with a random number between -alpha and alpha,
        # and return the new list created by that process

        random.seed(seed)
        d = list()
        for i in info:
            d.append(i + random.randint(-alpha, alpha))
        return d

    @staticmethod
    def recommend(model, distortedInfo):

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
        rec = model[0][1]
        for x in model:
            if s > x[0]:
                rec = x[1]
        return rec

    @staticmethod
    def alpha_bargain(c, v):
        return (c.preferredAlpha + v.preferredAlpha) / 2

    # def ContractExists(self, VendorID, ConsumerID):
    #     if VendorID in self.blockchain:
    #         if ConsumerID in self.blockchain[VendorID]:
    #             return True
    #     return False
    #
    # def makeContract(self, vendor, consumer, alpha):
    #     if self.ContractExists(vendor.getID(), consumer.getID()):
    #         return False
    #     if vendor.getID() not in self.blockchain:
    #         self.blockchain[vendor.getID()] = dict()
    #     self.blockchain[vendor.getID()][consumer.getID()] = consumer.getData(alpha)
    #     return True
    #
    # def getData(self, vendor, consumer):
    #     VendorID = vendor.getID()
    #     if VendorID in self.blockchain:
    #         ConsumerID = consumer.getID()
    #         if ConsumerID in self.blockchain[VendorID]:
    #             return self.blockchain[VendorID][ConsumerID]
    #     return False

    def incrementTime(self):
        self.time += 1

    # Based on section 2.3.2 RAM Reductions and TinyRAM:
    # https://madars.org/phd-thesis/Madars-Virza-thesis-20170831.pdf
    # While theoretical circuit size is O(TlogT + cT)
    # The authors demonstrate that O(cT) Dominates where c is a cpu transition function
    # Below I encode the T runtime for a KNN prediction
    def proofTime(self, K, n):

        i = 0
        #Evaluate Destance for k datapoints
        while i <= n:
            # Counter and arbitrary binary computation
            i = i + 1
        i = 0
        #Sort n points by distance using quicksort
        while i <= n*math.log(n):
            # Counter and arbitrary binary computation
            i = i + 1
        i = 0
        #Nearest neighbor voting for K nearest neighbors
        while i <= K:
            # Hashing the constant K should have a similar computational runtime as selecting from a hastable
            hash(K)
            # Counter and arbitrary binary computation
            i = i + 1
