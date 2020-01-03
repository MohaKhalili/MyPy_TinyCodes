# A function named items_price that accepts two lists as parameters. 
# The first list contains the quantities of n different items, the 
# second list contains the prices that correspond to those n items 
# respectively. Now, calculate the total amount of money required 
# to purchase those items. Assume that both the lists will have equal lengths.

def items_price(a, b):
    sum_price = 0
    for i in range(len(a)):
        sum_price = sum_price + (a[i] * b [i])
    return sum_price

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
result = items_price(my_list1, my_list2)
print(result)