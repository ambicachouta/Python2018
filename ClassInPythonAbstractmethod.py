from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod

    def calculate_salary(self,sal):
        pass
class Developer(Employee):

    def calculate_salary(self,sal):
        finalsalary = sal * 1.10
        return finalsalary
emp_1 = Developer()
print(emp_1.calculate_salary(10))


from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod

    def calculate_salary(self,sal):
        pass
emp_2 = Employee()
emp_2.sal = 1000
print(emp2.sal)

"""
OUTPUT:
    = RESTART: C:/Users/Jessicah Princess/Desktop/ClassInPythonAbstractmethod.py =
Traceback (most recent call last):
  File "C:/Users/Jessicah Princess/Desktop/ClassInPythonAbstractmethod.py", line 24, in <module>
    emp_2 = Employee()
TypeError: Can't instantiate abstract class Employee with abstract methods calculate_salary
>>>
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod

    def calculate_salary(self,sal):
        pass
class Developer(Employee):

    def calculate_salary(self,sal):
        finalsalary = sal * 1.10
        return finalsalary
    
    def position_1(self,position):
        self.position = postition
        return position

emp_1 = Developer()
#print(emp_1.calculate_salary(10))
print(emp_1.position_1('WebDeveloper'))

