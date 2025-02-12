from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name = name

    def breathe(self):
        print(f"Breathing")

    @abstractmethod
    def make_sound(self):
        pass