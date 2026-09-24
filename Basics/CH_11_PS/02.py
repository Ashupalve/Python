# 2. Create a class ‘Petsʼ from a class ‘Animalsʼ and further create a class ‘Dogʼ from ‘Petsʼ.
# Add a method ‘barkʼ to class ‘Dogʼ.

class Animal :
    pass

class pets(Animal):
    pass

class dog(pets):
    @staticmethod
    def bark ():
        print("Bow Bow")
d = dog()
d.bark()