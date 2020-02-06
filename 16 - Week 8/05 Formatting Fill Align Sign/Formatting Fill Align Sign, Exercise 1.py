# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match 
# the correct Python output.

my_string = "x = {0:%<7d} and y = {1:@>8d}".format(5, 43)
print (my_string)
###################################################################
my_string = "x = {0:#^7d} and y = {1:@>8.4f}".format(6, 0.2)
print (my_string)
###################################################################
my_string = "x = {0:*^7s} and y = {1:?<8.2f}".format("cat", 4.256)
print (my_string)
###################################################################
a = "john"
b = "happy"
my_string = "{0:*^10} is {1:+^9s}".format(a,b)
print (my_string)
###################################################################
a = "mary"
b = "fine"
my_string = "{0:5s} is {1:5s} and {}".format(a,b)
print (my_string)