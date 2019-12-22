# A function that finds the distance between two points and returns it. 
# The distance between two points with x,y, and z components can be 
# calculated as:

# distance=(x2−x1)2+(y2−y1)2+(z2−z1)2−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√
# The input for this function will be two 1 Dimensional lists that 
# contain the x,y,z coordinates each. 

# Type your code here
def Find_Distance(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    distance = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2 )**(1/2)
    return distance

def list1_create():
    lst = [] 
    # number of elemetns as input 
    n = 3
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter list one element : ")) 
  
        lst.append(ele) # adding the element
    return lst 

def list2_create():
    lst = [] 
    # number of elemetns as input 
    n = 3
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter list two element : ")) 
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
list_one = list1_create()
list_two = list2_create()
result = Find_Distance(list_one, list_two)
print("Distance between two points is : ",result)