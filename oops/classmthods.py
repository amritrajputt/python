class chaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def  from_dict(cls,order_data): #cls is reserved keyword for classmethod and it is necessary and should be 1st parameter
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["small","medium","large"]
    
print(ChaiUtils.is_valid_size("medium"))

order1 = chaiOrder.from_dict({"tea_type":"masala","sweetness": " low", "size":"medium"})    
print(order1.__dict__)    

#both static and class method dont have access to self