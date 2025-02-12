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



from abc import ABC, abstractmethod

class Shape(ABC):  # Inherit from ABC to make the class abstract
    @abstractmethod  # Decorator to define an abstract method
    def area(self):
        pass  # No implementation in the abstract class

class Circle(Shape):  # Concrete subclass of Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Must implement the abstract method
        return 3.14159 * self.radius**2

class Square(Shape):  # Another concrete subclass of Shape
    def __init__(self, side):
        self.side = side

    def area(self):  # Must implement the abstract method
        return self.side**2

# shape = Shape()  # This will raise a TypeError: Can't instantiate abstract class Shape

circle = Circle(5)
print(circle.area())  # Output: 78.53975

square = Square(4)
print(square.area())  # Output: 16

# Polymorphism:
shapes = [circle, square]
for shape in shapes:
    print(shape.area())  # Call the appropriate area() method for each shape