# Write a program that asks the user for an input and tries to 
# handle the error that may occur when you try to type cast the 
# input to an int using the try ... except ... else clause. 

# Your function should print the result if the operation is 
# successful, if the operation is not successful your program 
# should print 'Error'

my_input = input("Please enter something: ")
try:
    x = int(my_input)
    print(x)
except ValueError:
    print('Error')