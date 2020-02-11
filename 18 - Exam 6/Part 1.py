# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

my_string = "x = {1:5.2f} and y = {0:3d}".format (14 , 3.5)
print (my_string)
#############################################################################
my_string = "x = {} and y = {}".format (5,"pet")
print (my_string)
#############################################################################
my_string = "x = {} and y = {}".format (2.3)
print (my_string)
#############################################################################
my_string = "x = {2} and y = {1}".format ( "cat", 2.3, "pet")
print (my_string)
#############################################################################
my_string = "x = {1:5.2f} and y = {0:5d}".format (13 , 5.2645326)
print (my_string)
#############################################################################
my_string = "x = {0:4d} and y = {1:3d}".format ("dog" , 1)
print (my_string)
#############################################################################
my_string = "x = {0:#^7d} and y = {1:@>8.3f}".format(2, 0.6)
print (my_string)
#############################################################################
a = "jack"
b = "sad"
my_string = "{0:*^12} is {1:+^7s}".format(a,b)
print (my_string)
#############################################################################
print('X{0:Y^9}Z'.format('cat'))
#############################################################################
print('B{0:,}C'.format(123456789))