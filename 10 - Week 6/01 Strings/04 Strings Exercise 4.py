# A program that asks the user for an input 'n' and prints a square 
# of n by n asterisks "*". For example if the user enters 5 then the 
# output should look like the following: Note that there should be no
# spaces between the asterisks

# *****
# *****
# *****
# *****
# *****

# Type your code here
number = int(input("Please enter the number : "))
for i in range(1, number+1):
    print(number*'*')