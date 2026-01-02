# Exception handling
# errors -- runtime error , compile time error
# exception : runtime error types 
# for un wanted behaviours it throw an error (execption at runtime)

# how to handle it using try-except

# example

try:
    b=0
    if(b==0):
        raise Exception({
            "error":"Zero divison error",
            "status":False
        }) # this is catch in except block i array form 
        # it is similar to throw error() in js
except Exception as e:
    print("errors are " , e.args[0]['status'])
