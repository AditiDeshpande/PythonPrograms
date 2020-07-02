#Functional Programming
#Decorators are the functions who takes functions
#as parameters and returns the modified version
#of that functions

#Real life example is if u want to execute some code only when user
#is logged in then u can use these Decorators

#so in following line f = hello function
def announce(f):
    def wrapper():
        print("About to run the function..")
        f() #hello function which is printing Hello , World!!
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello , World!!")

hello()

#output
# About to run the function..
# Hello , World!!
# Done with the function
