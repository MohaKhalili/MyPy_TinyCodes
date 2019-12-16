# a function that finds the magnitude of a given 3-dimensional vector. 
# The magnitude of a vector is the square root of sum of squares of all
# the components of the vector.

# magnitude=x2+y2+z2−−−−−−−−−−√)
# Your input for this function will be a (vector with x,y,z components) a 
# list containing 3 integers i.e, [x,y,z]. 

# For example if the input list is:
# vector = [2, 3, -4]
# Then you should return the magnitude (as a floating point number) of this vector:
# 5.385164807134504

# Type your code here
def altitude(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    number = ((x**2) + (y**2) + (z**2))**(1/2)
    return number