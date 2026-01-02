def factorialCal(num):
    retVal=1
    while num:
        retVal*=num
        num=num-1
    return retVal
print("the factorial of 6 : " , factorialCal(6))        


#lets learn about array and string
# arr={1 , 3, 4, 8 ,5 ,6}

list1=[1, 2]
list2=[1]
print(list1 is not list2)  # it is use to comapare the reference val
print(list1 == list2)

#logical operator
a=100
b=0
print(a>10 and b<8) # similary "or" , "not" exist

# membership does val exist or not
strlist=['a' , 'd' , 'e']
print('a' in strlist) # similarly is not also exist


# lets learn about for loop

# str="abcd" it also work in list  , tuple , etc
# for char in str:
#     print(char)

# how to use range(start , end  , step) in for loop (exclusive in nature)
for i in range(1, 5): # it run from 1->4 exclusive in nature [1,5)
     print(i)
    
# by default step=1 , you can modify it accordingly
for i in range(1, 100 , 2): # prints odd val till 99
    print(i)


# range() it returns a list of val from start to end-1
print(list(range(1, 5)))  #type conversion -- [1 , 2 , 3 , 4]

# break is use to break the loop
# continue is use to skip that iteration
# pass is use so that if youd dont want to exe in a loop you can add pass statement


# lets talk about string
#'str'  "str" , '''str''' , """str""" there are four ways to write str value
'''
how to find length of string -- len(var)
how to do indexing in string

str="array"
str[0] -- in str index start from 0 --->   len(str)-1

slicing concept of string
if you want ot get some order part of string then you can use slicing methos


how --- str[firstIndex:lastIndex:step] all are sperated by colon (:)

for full string you can use str[:]
for full string you can use str[::]
you can also revers it using this operator : str[::-1]





'''

sentence="hi my name is ritesh"
str="name is ritesh"
print(sentence[0:4:1]) # output is "hi m"
print(sentence[::-1]) # hsetir si eman ym ih
print("rit" in sentence)  # similarly "not in" also exist , it is use to check whether the substr present or not
# some more str operations
print(str.capitalize() , " " , str.lower() , " " , str.find("name") , " " , str.upper())

str=str.split(" ")
print("-".join(str))


'''
lets talk about list

how to declare and init 
list_1=[1 ,  ,  ,  ,....]
list are heterogeneous in nature
list are multable in nature
list are order in nature
list support duplicate values;

'''

list_1=[1 ,2 ,4, 5,True , False  , "hello"]
print(list_1)

# how to append new value in list
list_1.append(5);
print(list_1)
#how to remove ele from list
list_1.remove(1)   #it will remove first occurence of elem and it return None
print(list_1)

list_1=list_1.__add__([1, 3])  # add new list at the end
print(list_1)
print(list_1.count(2))


# how to copy list

list01=[1, 2]
list02=list01 # this is shallow copy , whatever you change i =n list01 it will reflect in list02
list02=list02.copy() # this is deep copy 


# how to add another list at the end
list_1.extend(list01)
print(list_1)

list_1.insert(2,[1 , 3] )
print(list_1)

#remove nd pop method also clear
# list_1.remove(val) it remove first occurrence of that val
# list_1.pop(index) it remove the index value of that list and return that value
# list_1.clear() remove all the elements
# list_1.sort()
print(len(list_1))


'''
list comprehension
[expression item in iterable if condition]
add expression , then item in iterable , and at las condition(optional)
example : create a list of 5 number divisble by 2 starting from val-2
list=[i**2 for i in range(1, 6)]
'''
list04=[i**2 for i in range(1, 6)];  #square of number from 1-->5
print(list04)
# you can also add if-else
list04=[i**2 for i in range(1, 6) if i%2==0] #those square which are even number
print(list04)


'''
tuples : init  immutable , hetereogeneous in nature , supports all immutable methods of list
a=(2 ,  3, 4)

'''





'''

now the most imp concept of python (storing data  commonly used in creation of api) i.e dictionary
it is simlar to an object of javascript
dictionary is in ordered in nature but before V3.7 it was unordered



obj={
"name":"ritesh",
"age":24,
"phone_no":3439483948394


}
 how to access : two methods are there obj["key"] , obj.get("key"){it does not throw error if key does not presnt insted of that it return None
 }

 how to append new key:val
 same obj["key"]=val (if exist then update the value ) otherwise create a new key:val

 how to delte  a key:value

 del obj["key"]  or obj.pop(key) - return val or none
 obj.popitem() delte last element of the dictionary
 obj.clear() remove all the key:values


 how to get key , value
 obj.keys() , obj.values() , obj.items() -- it will return the key:value pairs in tuple form (list(obj.items()) it will convert into list of tuples

- lets talk about dict comphersion
obj1={x:x**2  for x in range(1, 5)}
obj1-{
1:1 , 2:4 , 3: 9 , 4:16}



'''
obj1={x:x**2  for x in range(1, 5)}
print(obj1)
obj2={x:x**2  for x in range(1, 5) if x%2==0}
obj={
"name":"ritesh",
"age":24,
"phone_no":3439483948394


}

''' how to use for loop in dict
   for keys in dict:
    print(keys)

'''
for keys in obj:
    print(keys) # it return the keys of this object
    print(obj[keys]) # it return the value of each key of this obj
print(obj.values() , obj.items()) #, etc    





'''
lets talk about funtion

decl:

def function_name(params...):
    //code....


there are diff ways to pass value of each para
function_name(para1, para2 , para3=default_value) if para3 value is not passed then take default value
function_name(param1=default_val)
one things deafult value should be the last param value or all param will have been the default_value




'''


# def printVal(list1=[12] ):
#     for item in list:
#         print(item)
# printVal(list_1)     # calling a funtion with arg


def function_naem(p=2 , c=2):
    pass


''' important concept --- what is decorator (it is nothing but a function that called another function before calling that fucntion)
'''

def custom_decorator(cb_fun):
    #you can do anythings before calling the main function
    print("before the call back function")
    def call(a, b):
      cb_fun(a,b)
    return call


# how to use decorator
@custom_decorator
def cb_fun(a,b):
    print("callback function called")
    return a+b
cb_fun(2 , 3);    



'''generators
      def func(a):
        while a:
            yield(a)
            a-=1
      how to use it 
      for i in func(5):
        print(i)
// here it stores the previous value and return it in next call
'''
def func(a):
    while a:
         yield(a)
         a-=1
    #   how to use it 
for i in func(5):
        print(i)


'''
lambda function or anonomous function
itis use to fast execution inline function(takes only one express)
lambda x:expression 

square = lambda lst: [i * i for i in lst] this is how to use for loop
print(square([1, 2, 3, 4]))


''' 

return_val=lambda x:x**2 
print(return_val(2))


''' 
how to create a class and object



'''
