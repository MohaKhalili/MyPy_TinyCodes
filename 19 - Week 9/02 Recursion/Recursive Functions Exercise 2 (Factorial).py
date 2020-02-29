# A function named calculate_factorial that receives a positive integer 
# 'n' as parameter and calculates and returns the factorial of n using 
# recursion.

# Factorial is the product of an integer with all the integers below it. 
# For example, the factorial of 5 is 5*4*3*2*1 = 120. Note that the factorial 
# of both 0 and 1 is 1. For example, when your function is called as:
# calculate_factorial(10)
# Then, your function should return the number:
# 3628800

################### My Solution ###################
def calculate_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

################### Driver Code ###################
number = int(input("Please enter your number for factorial calculation : "))
result = calculate_factorial(number)
print(result)
