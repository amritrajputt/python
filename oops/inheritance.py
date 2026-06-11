class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai")

class MasalaChai(BaseChai): #using paranthesis to inherit from BaseChai

    def prepare(self):
        print(f"Preparing {self.type} chai with spices")

class ChaiShop():
    chai_cls = BaseChai #class variable to hold the chai class. this is called composition
    def __init__(self, chai_type):
        self.chai = self.chai_cls("Regular")

    def serve_chai(self):
        print(f"Serving {self.chai.type}")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop("regular")
fancy = FancyChaiShop("kadak")
shop.serve_chai()
fancy.serve_chai()
fancy.chai.prepare()