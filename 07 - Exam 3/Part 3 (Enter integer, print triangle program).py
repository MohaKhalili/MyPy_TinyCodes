# What will be printed after each of the following code segments? If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the correct Python output.

# a program that asks the user for a positive number 'n' as input. Assume that the user enters
# a number greater than or equal to 3 and print a triangle as described below. 

# For example if the user enters 6 then the output should be:

# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *

# Type your code here
n = int(input("please enter the number: "))
i = 1
Str = "*"
while i <= n:
    k = i * Str
    print(k)
    i = i+1
i = i-2
while i > 0:
    k = i * Str
    print(k)
    i = i - 1