from multiprocessing.managers import BaseManager


class Fruits:
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"My favorite fruits is: {self.name} its {self.shape} in shape and cost {self.price}")

#instance of a class
myobj=Fruits(price: 20, shape: "oval", name: "Banana")
myobj.display()