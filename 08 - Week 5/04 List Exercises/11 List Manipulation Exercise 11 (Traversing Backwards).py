# A function that accepts a list and returns a new list such that 
# the new list contains all the items of the old list in reverse 
# order. Note that this is NOT a sorting problem. Do NOT use the 
# built in reverse() method for this problem. For example if:

# input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']

# then your function should return a list such as:
# ['I', 'Love', 'Grapes', 'but', 'I', "don't", 'eat', 'apples']

def Traversing_Backwards(my_list):
    output = []
    for i in range(len(my_list)):
        output.append(my_list[-i-1])
    return output

# getting list from input
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of list elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = input("enter the list element : ")
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = Traversing_Backwards(my_list)
print(result)

################### Sample Solution ###################
# def _reverse_of_a_list_sample_(old_list):
#     new_list = []
#     length = len(old_list)
#     i = -1
#     # Iterate the list using negative indices
#     while i >= -length:
#         new_list.append(old_list[i])
#         i = i - 1
#     return new_list