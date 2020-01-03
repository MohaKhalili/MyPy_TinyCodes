# A function that accepts two lists both of which consists of numbers 
# and returns the total sum of all the even numbers integers from both 
# lists. If there are no even numbers in the list, the function should 
# return 0.

# Type your code here
def Sum_Even_Numbers(list1 , list2):
    sum_num = 0
    one_list = list1 + list2
    for item in one_list:
        if item % 2 == 0:
            sum_num += item
    return sum_num

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
my_list1 = list_create()
my_list2 = list_create()
result = Sum_Even_Numbers(my_list1, my_list2)
print(result)

################### Sample Solution ###################
def _sum_of_evens_sample_(a, b):
    total_sum = 0
    for items in a:
        if items % 2 == 0:
            total_sum = total_sum + items
    for items in b:
        if items % 2 == 0:
            total_sum = total_sum + items
    return total_sum