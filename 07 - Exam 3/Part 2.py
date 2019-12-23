# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

def say_hello():
    print('Hello Universe!') 
say_hello()

###################################################################
def func(x):
    x = 2
    print('x is', x)
func(50)

###################################################################
def even(x):
    if x % 2 == 0:
        return x
    else:
        return x+1
print(even(3))

###################################################################
def cube(x):
    return x * x * x   
y = cube(3)    
print(y)

###################################################################
def fun(x, y, z): 
    z = x * y
    return x + y + z
print(fun(2, 30))

###################################################################
def find_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
find_max(3, 4)

###################################################################
def my_fun(x):
    count = 0
    for str in x:
        if str == "cat":
            count = count + 1
        elif str == "dog":
            count = count - 1
    return count
z = ['cat', 2, 'cat', 'dog', 34, 'cat'] 
print(my_fun(z))

###################################################################
def myFun():
    count = 0
    for x in range (0,3): 
        count = count + x
    return 
print(myFun())

###################################################################
def fun1(x,y):
   z = multiply(x,y)
   m = x + z
   return m
  
def multiply(a,b):
   n = a * b
   return n
  
x = 2
y = 4
z = fun1(x,y)
print (x,y,z)

###################################################################
def my_fun(x):
    for m in range(0,3):
        n = 2
        while n <= 4:
            if m == n:
                x = x + 1
            n = n + 1
    return x
print(my_fun(5))