# A function that normalizes a vector (finds the unit vector). 
# A vector can be normalized by dividing each individual component 
# of the vector by its magnitude. Your input for this function will be
# a vector i.e. 1 dimensional list containing 3 integers. 

# For example if the input list is:
# vector = [2, 3, -4]
# Then you should return the unit vector(1-Dimensional list) such as:
# [0.3713906763541037, 0.5570860145311556, -0.7427813527082074]

# Type your code here
def unit_vector(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x**2) + (y**2) + (z**2)) ** (1/2)
    
    VECTOR = [x/mag, y/mag, z/mag]
    return VECTOR

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
result = unit_vector(my_list)
print(result)