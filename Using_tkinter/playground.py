#Unlimited argu,ents function. the asteric sign is key it saves all the input as tuple and can be accessed positionally
def Add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(Add(2,3,4,5,6))

#keyword arguments allows for multiple keyword to be use i the fucntion
#This basicaslly stored the input as a dictionary that can be access by it keyword
def keyword(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n -= kwargs["subtract"]
    print(n)

keyword(3, add=4, subtract=5)

class Car:
    def __init__(self, **kwar) -> None:
        #the get can be used to egt a keyword but it doesn't crash when  n value is attached to it in init
        self.make = kwar.get("make")
        self.model = kwar.get("model")

car = Car(make="Nissan")

print(round(1.997))