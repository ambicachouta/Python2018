class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')


Smallcar = Car()
Smallcar.drive()
Smallcar._Car__updateSoftware()  #not accesible from object.
#AttributeError: 'Car' object has no attribute '__updateSoftware'

'''
public methods		Accessible from anywhere
private methods		Accessible only in their own class. starts with two underscores
'''