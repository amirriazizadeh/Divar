
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        else:
            print("Returning existing instance")
        return cls._instance

    

s1 = Singleton()
s2 = Singleton()
s3 = Singleton()
print(s1 is s2)  

# ===============================================================

class Add:
    def __init__(self, value=0):
        self.total = value

    def __call__(self, value):
        return Add(self.total + value)

    def __str__(self):
        return str(self.total)

    __repr__ = __str__ 



print(Add(10))             
print(Add(10)(11))         
print(Add(10)(11)(12))     


# ================================================================




