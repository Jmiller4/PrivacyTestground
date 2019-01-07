import random
import hashlib

class Entity:

    def __init__(self, fed):
        self.alphaPreference = random.random()
        self.agreements = dict()
        self.fed = fed
        self.preferredAlpha = random.uniform(0, 5) * 2
        self.id = self.generate_id()
        self.fed.addMember(self, self.id)

    # "agreements" should be a record of all the info exchange agreements an entity has with others
    # indexed by id first, which goes to a second dictionary of info about the other party

    def generate_id(self):
        id = random.getrandbits(16)
        while id in self.fed.IDs:
            id = random.getrandbits(16)
        return id

    def add_agreement(self, t, id, alpha):
        self.agreements.append((t, id, alpha))

    def get_id(self):
        return self.id