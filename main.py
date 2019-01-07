from consumer import *
from vendor import *
from federation import *



fed = Federation()

consumers = list()
vendors = list()
for x in range(3):
    c = Consumer(fed)
    consumers.append(c)
    print(c.id)
    v = Vendor(fed)
    vendors.append(v)
    print(v.id)

print(fed.blockchain_to_string())

for t in range(10):
    for c in consumers:
        for v in vendors:
            if random.random() < 0.1:
                c.exchange(v, t)

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
