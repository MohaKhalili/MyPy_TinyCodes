# a program using while loops that asks the user for a positive 
# integer 'n' and prints a triangle using numbers from 1 to 'n'.
n = input("please enter a number form 1 to n: ")

i = 1
while i <= int(n):
    my_str = i*str(i)
    print(my_str)
    i = i + 1