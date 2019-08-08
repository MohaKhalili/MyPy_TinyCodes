# a program that asks the user for an input 'n'
# and prints a square of n by n asterisks "*". 

n = int(input("please enter the number: "))

i = 1
while i <= n:
    my_str = n * "*"
    print(my_str)
    i = i + 1