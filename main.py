from consumer import *
from vendor import *
from federation import *
import sys


fed = Federation()

consumers = list()
vendors = list()

# this part of the code simulates vendors and consumers joining the federation
for x in range(3):
    c = Consumer(fed)
    consumers.append(c)
    print("consumer", c.id)
    v = Vendor(fed)
    vendors.append(v)
    print("vendor", v.id)

# this part of the code simulates vendors and consumers learning about the other parties
# right now, consumers only know the vendors, and vendors only know about the consumers
# (so, vendor A and vendor B don't "know" about each other's existence (really, they just don't keep pointers to each other))
for l in vendors, consumers:
    for e in l:
        e.updateKnowledgeOfOtherParties()

# print(fed.blockchain_to_string())

# this part simulates the operation of the system over time
for t in range(10):

    # first, update everybody on what time it is
    for l in vendors, consumers, [fed]:
        for e in l:
            e.incrementTime()

    for c in consumers:
        if random.random() < 0.1:
            c.initiateExchange

print(fed.blockchain_to_string())


# User1 = consumer()
# User1.generateData()
# print(User1.toString())
# User2 = consumer()
# User2.generateData()
# print(User2.toString())
# User3 = consumer()
# User3.generateData()
# print(User3.toString())
# User4 = consumer()
# User4.generateData()
# print(User4.toString())
#
# Vendor1 = vendor()
# print(Vendor1.getID())
# Vendor2 = vendor()
# Vendor3 = vendor()
# print(Vendor2.getID())
# print(Vendor3.getID())
#
# fed = federation()
#
# #Alpha is hard coded at 2 since it may be negotiated by parties
# fed.makeContract(Vendor1, User1, 2)
# print(fed.getData(Vendor1, User1))
# fed.makeContract(Vendor1, User2, 2)
# print(fed.getData(Vendor1, User2))
# fed.makeContract(Vendor2, User3, 2)
# print(fed.getData(Vendor2, User3))
# fed.makeContract(Vendor2, User4, 2)
# print(fed.getData(Vendor2, User4))
# fed.makeContract(Vendor3, User1, 2)
# print(fed.getData(Vendor3, User1))
#
