class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

# Object is created and we are calling a class part of an object
Smallcar = Car()

# Calling a public method which is part of a class i.e. Car
Smallcar.drive()

# Calling a Private variable which is part of a class i.e. Car
Smallcar.__maxspeed = 10  # will not change variable because its private

# Calling a public method which is part of a class i.e. Car
Smallcar.drive()