# Write a function that accepts a number x and evaluates the following expression:

# y=abs(x3)+cos(3x−−√)

# and returns the value of y. Hint: Use the math module!

# Type your code here
import math
def Evaluate_Expression(x):
    y = abs(x**3) + math.cos(math.sqrt(3*x)) 
    return y