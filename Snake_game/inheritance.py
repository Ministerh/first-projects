#Inheritance
class Animal:
    def __init__(self) -> None:
        self.num_eye = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    'this class will inherit from the super class'
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("this is done under water")

    def swim(self):
        print("moving in water")


huz = Fish()
huz.breathe()
huz.swim()
print(huz.num_eye)