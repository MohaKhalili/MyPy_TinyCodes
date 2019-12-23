# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

# a program that asks the user for a positive number 'n' as input. 
# Assume that the user enters
# a number greater than or equal to 3 and print a triangle as 
# described below. 

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

# method 1 (while loop)
n = int(input("please enter the number, then I'll give you two symmetric riangle (with while loop): "))
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

# method 2 (for loop)
n = int(input("please enter the number, then I'll give you two symmetric riangle (with for loop): "))
for i in range(1,n+1):
    x = i * "*"
    print(x)
    if i == n:
        for j in range(n-1,0,-1):
            x = j * "*"
            print(x)

################### Sample Solution ###################
n = int(input("Please enter an integer: "))
for x in range(1, n+1):
    print("*" * x)
for y in range(n-1, 0, -1):
    print("*" * y)