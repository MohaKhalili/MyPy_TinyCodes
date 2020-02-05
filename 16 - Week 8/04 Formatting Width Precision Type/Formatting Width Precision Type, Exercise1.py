# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

my_string = "x = {1:5.2f} and y = {0:3d}".format (14 , 3.5)
print (my_string)
#######################################################################
my_string = "x = {0:4d} and y = {1:3.4f}".format (5 , 1.0)
print (my_string)
#######################################################################
my_string = "x = {0:4d} and y = {1:3d}".format ("dog" , 1.0)
print (my_string)
#######################################################################
my_string = "x = {0:6s} and y = {1:4.3f} ".format ("cat" , 1.23456)
print (my_string)
#######################################################################
my_string = "x = {1:4d} and y = {0:4s}".format ("dog" , 1.0)
print (my_string)