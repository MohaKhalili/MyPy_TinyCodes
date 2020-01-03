 # A function named crazy_list that accepts a list as parameter and 
 # returns a boolean (either True or False) based on whether or not 
 # the list is the same forward and backwards. You may NOT use list.reverse() method. 

# Type your code here
def crazy_list(some_list):
    situ = True
    for i in range(len(some_list)):
        if some_list[i] != some_list[-1-i]:
            situ = False
    return situ            

def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter list element : ")) 
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = crazy_list(my_list)
print(result)


################### Instructor function ###################
def _test_list_palindrom_sample_ed2(some_list):
    size = len(some_list)
    if size % 2 == 0:
        # if the length is even
        mid = int(size / 2)
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid::][::-1]
    else:
        mid = int((size ) / 2)
         # get the first half
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid+1::][::-1]
    if first_half == second_half:
        return True
    else:
        return False