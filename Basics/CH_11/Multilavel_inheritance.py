class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)
# print(o.c) # Shows an error as therre is no c attribute in programmer class


o = Manager()
print(o.a, o.b, o.c)  # here all attributes are acessible beacause of multilevel inheritance