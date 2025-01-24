class Animal:
    def breathe(self):
        print("Breathing")


class Fish(Animal):
    def swim(self):
        print("Swimming")


class Human(Animal):
    def walk(self):
        print("Walking")


animal = Animal()
animal.breathe()

fish = Fish()
fish.breathe()
fish.swim()


human = Human()
human.breathe()
human.walk()
