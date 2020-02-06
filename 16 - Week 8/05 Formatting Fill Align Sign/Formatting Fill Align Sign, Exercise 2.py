# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match 
# the correct Python output.

my_string = "x = {1:*>6.4f} and y = {1:+5.3f}".format(2.3, -4.12345678)
print (my_string)
####################################################################
# my_string = "x = {1:*3d} and y = {0:-4.2f}".format(5, -0.5)
# print (my_string)
####################################################################
my_string = "x = {0:+4.2f} and y = {1:+5.3f}".format(3.45, -2.23)
print (my_string)
####################################################################
my_string = "x = {0:-3.1f} and y = {1:+3.2f}".format(2.44, -3.76)
print (my_string)
####################################################################
my_string = "x = {0: 3d} and y = {1:+4d}".format(223, -45)
print (my_string)