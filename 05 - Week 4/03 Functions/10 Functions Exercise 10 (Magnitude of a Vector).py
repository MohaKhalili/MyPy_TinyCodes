# A function that finds the magnitude of a given 3-dimensional vector. 
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

def list_create():
    lst = [] 
    # number of elemetns as input 
    n = 3 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter 3-dim vector element : ")) 
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = altitude(my_list)
print(result)