class Plant:
    moves = False
    def breathe(self):
        print("Breathing")





class Animal:
    moves = True
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
print(fish.fins)

human = Human()
human.breathe()
human.walk()
