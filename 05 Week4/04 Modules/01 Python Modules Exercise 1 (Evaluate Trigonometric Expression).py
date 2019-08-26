# a function that accepts a number x and evaluates the following expression:

# y=sin(x)−cos(x)+sin(x)cos(x)

# and returns the value of y. (Hint: Use math module)

# Type your code here
import math
def Evaluate_Trigonometric_Expression(x):
    y = math.sin(x) - math.cos(x) + math.sin(x) * math.cos(x)
    return y