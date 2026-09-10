def f1():
    x=10 # x is local variable 
y=10 #y is globasl variable
    

#nested list in function
def f1():
    # Local variable inside f1
    x = 10 
    
    # f2 is now a nested function (defined inside f1)
    def f2(value):
        # Can access x from the outer function
        print(f"Inside nested f2: value received is {value}, outer x is {x}")
        print("{} is  {}".format(value,x))
    
    # Calling the nested function inside f1
    f2("number") 

# Run the outer function
f1()

def f2():
    x=100

    def f3(value):
        print("{} is inside {}".format(value,x))
    f3("hello")

f2()        

