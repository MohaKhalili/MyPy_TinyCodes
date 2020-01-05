# A function that takes a list of words as an input argument and 
# returns True if the list is sorted and returns False otherwise.

def Sorted_Test(String_list):
    IsSorted = False
    new_string = sorted(String_list)
    if new_string == String_list:
        IsSorted = True
    return IsSorted

# getting string list from input
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = input("enter list element : ")
        lst.append(ele) # adding the element
    return lst 

# Driver code test
input_str = list_create()
result = Sorted_Test(input_str)
print(result)