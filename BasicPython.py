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
