# class and objects

# class Person:
#     def speak(self):
#         print("someone is speaking")

#creating an object

# p1=Person()
# p1.speak()


# advance concept
class Person:
    def __init__(self , name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender
    def speak(self):
        print(f"{self.name} is speaking")

person1=Person("ritesh"   , 24 , "male")
person1.speak()


# lets create a class with var in diff ways

class Animal:
    # name,no_of_legs
    def __init__(self  , n , l):
        self.name=n
        self.no_of_legs=l
    def animalType(self):
        print(f"animal name is {self.name} and has {self.no_of_legs} legs")    

animal01=Animal("dog" , 4)     
animal01.animalType()    # internally python calls Animal.animalType(instance_name)     , thats why it is required to pass self so that it does not get confused regarding the data of each instance

