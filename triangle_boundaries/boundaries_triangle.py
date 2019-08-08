# a program that asks the user for an input 'n' 
# (assume that the user enters a positive integer) 
# and prints only the boundaries of the triangle 
# using asterisks "*" of height 'n'.

n = int(input("please enter a number: "))
i = 1
while i <= n:
    if i == 1:
        print("*"*n)
    elif i < n:
        print("*",end = "")
        print((n-i-1)*" ",end = "")
        print("*")
    else:
        print("*")
    i = i + 1