from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("We can walk!")

class Dog(Animal):
    def move(self):
        print("We like to eat meat!")

class Cat(Animal):
    def move(self):
        print("We eat milk!")

obj1 = Human()
obj1.move()
obj2 = Dog()
obj2.move()
obj3 = Cat()
obj3.move()


