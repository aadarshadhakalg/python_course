class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sleep(self):
        print(f"{self.name} slept")

    def talk(self):
        print(f"{self.name} is speaking!")

aayush = Person("Aayush", 26)
manish = Person("Manish", 30)

print(aayush.name)
print(manish.name)
aayush.sleep()
manish.talk()