#!/usr/bin/python
# polymorphism.py
class Animal:
   def __init__(self, name=''):
      self.name = name

   def talk(self):
      pass  # Empty

class Cat(Animal):
   def talk(self):
      print (self.name,"Meow!")

class Dog(Animal):
   def talk(self):
      print (self.name,"Woof!")

a = Animal()
a.talk()

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()

