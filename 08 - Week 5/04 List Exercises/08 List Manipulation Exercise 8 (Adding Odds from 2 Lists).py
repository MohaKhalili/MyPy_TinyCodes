# A function that accepts two lists both of which consists of integers 
# and returns the total sum of all the odd integers from both lists.

# method 1
def Adding_Odds_from_2Lists(my_list1, my_list2):
    one_list = my_list1 + my_list2
    sum_num = 0
    for element in one_list:
        if element % 2 != 0:
            sum_num = sum_num + element
    return sum_num

# method 2
def Adding_Odds(List1, List2):
    MyList = []
    for i in range(len(List1)):
        if List1[i] % 2 != 0:
            MyList.append(List1[i])
    for i in range(len(List2)):
        if List2[i] % 2 != 0:
            MyList.append(List2[i])
    sum_List = 0
    for i in range(len(MyList)):
        sum_List = sum_List + MyList[i]
    return sum_List

# getting list from input
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of list elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter the list element : "))
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list1 = list_create()
my_list2 = list_create()
result = Adding_Odds_from_2Lists(my_list1, my_list2)
print(result)