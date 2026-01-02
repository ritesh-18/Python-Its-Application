# inherit the property of parent class


class Bird:
    def __init__(self):
        print("bird is ready")
    def sound(self):
        print("sound is making")

class Parrot(Bird):
    def __init__(self):
        super().__init__()
        print("parrot is ready")  


parrot=Parrot()
#here you can access the property and method of Bird
parrot.sound()



# you can also inherit multiple class property

class InhertPro(Bird , Parrot):
    pass


# you can also override the parent methods (this is the polymorphism property)

'''
Method overriding is when a child (subclass) provides its own implementation of a method that is already defined in its parent (superclass).

'''

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   # overriding
        print("Dog barks")

'''
 Python does NOT support traditional method overloading like Java or C++.   

 Python does NOT have true public, protected, or private access modifiers.
 Python uses naming conventions, not enforced access control.

 private : double underscore before the var name (both for method , data member)
u = User()
u.__encrypt()      #  AttributeError
u._User__encrypt() #  works

 eg : __name : it is private var not accessible outside the class even in inherit class too

 public: single underscore before the var name
 eg: _name : accessible in inherit class but not outside      


use getter setters to get and set the data 

 
 '''

# lets talk about abstraction
'''

 Abstraction in Python means showing what an object can do while hiding how it does it.
Python does this mainly using abstract base classes (ABC).

------------------------------------------

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


def process_payment(payment: Payment):
    payment.pay(100)

process_payment(UPIPayment())
process_payment(CardPayment())

-----------------------------------------------------------
'''
