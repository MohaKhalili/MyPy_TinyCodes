# A program that asks the user for an input 'n' (assume that the user 
# enters a positive integer) and prints only the boundaries of the 
# triangle using asterisks "*" of height 'n'. For example if the user 
# enters 6 then the height of the triangle should be 6 as shown below 
# and there should be no spaces between the asterisks on the top line:

# ******
# *   *
# *  *
# * *
# **
# *

# method 1
number = int(input("Please enter the number : "))
for i in range(1, number+1):
    if i == 1:
        print(number*"*")
    elif i > 1 and i < number:
        print("*" + (' ' * (number-i-1)) + "*")
    else:
        print("*")

# method 2
# n = int(input("please enter a number: "))
# i = 1
# while i <= n:
#     if i == 1:
#         print("*"*n)
#     elif i < n:
#         print("*",end = "")
#         print((n-i-1)*" ",end = "")
#         print("*")
#     else:
#         print("*")
#     i = i + 1

################### Sample Solution ###################
# n = int(input("Please enter a positive integer: "))
# if n > 1:
#     print (n*"*")                     # Print the top line
#     for x in range(n-1, 1, -1):
#         print("*"+ (x-2)*" "+"*")     # Print the middle lines
#     print("*")                        # print the bottom line
# elif n == 1:
#     print("*")