from abc import ABC,abstractmethod

#ABC = Abstract Base Class
class Animal(ABC):

    def __init__(self,name):
        self.name = name

    def breathe(self):
        print(f"Breathing")

    @abstractmethod
    def make_sound(self):
        pass



class Dog(Animal):
    def make_sound(self):
        print("Barks!")


class Human(Animal):
    def make_sound(self):
        print("Speaks!")


## Error Abstract Method Cannot Be Instantiated
# animal = Animal("Hello")
# print(animal.name)

jimmy = Dog("Jimmy")
print(jimmy.name)
jimmy.make_sound()

aashish = Human("Aashish")
print(aashish.name)
aashish.make_sound()