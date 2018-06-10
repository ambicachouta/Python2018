A six part series I put together on object-oriented programming in Python.

1) Classes and Instances
2) Class Variables
3) classmethods and staticmethods
4) Inheritance - Creating Subclasses
5) Special (Magic/Dunder) Methods
6) Property Decorators - Getters, Setters, and Deleters

'''---------------------------------------------------'''
Classes :
'''---------------------------------------------------'''
    1. What is class :
                    Human 
       Properties:       Methods:
    Name                    Speaks
    Gender                  Do work
    Occupation              Sleeps
'''---------------------------------------------------'''
    2. What is object: Object is nothing but a specific instance of a class
        Object of class "Human"
Properties:    
    Name : Vin Diesel
    Gender: Male
    Occupation: Actor
Methods:
    Speaks : xxx return-2
    Do Work: Shoot Movies

Properties:    
    Name : Enrique Iglesias
    Gender: Male
    Occupation: Singer
Methods:
    Speaks : escape
    Do Work: Makes Music Albums
    
'''---------------------------------------------------'''        
    3. Write class in python:

#!/usr/bin/python

class Human:
    def __init__(self, n, o):
        self.name = n         # Properties of Human Class
        self.occupation = o   # Properties of Human Class
    def do_work(self):     # Method of class
        if self.occupation == "singer":
            print(self.name,"Sings songs")
        elif self.occupation == "actor":
            print(self.name,"Acts in Films")
    def speaks(self):      # Method of class
        print(self.name,"Says how are you?")

abiel = Human("vin diesel","actor")
abiel.do_work()
abiel.speaks()

enrique = Human("Enrique Abiel","singer")
enrique.do_work()
enrique.speaks()

'''-------------
