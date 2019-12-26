# A function that accepts a list of integers and returns a new list
# which is the sorted version (ascending order) of the original list
# (Original list should not be modified). You may NOT use the built 
# in sort() or sorted() functions. Notice that the original list should 
# not be modified.

# method 1
def List_Sorting(my_list):
    i = len(my_list)
    output = []
    while i != 0:
        output.append(min(my_list))
        my_list.pop(my_list.index(min(my_list)))
        i = i - 1
    return output

# method 2
def sorting_list(MyList):
    sorted_List = []
    i = 0
    while len(MyList) > 0 :
        min_num = MyList[0]
        for j in range(len(MyList)):
            if min_num > MyList[j]:
                min_num = MyList[j]
        sorted_List.insert(i,min_num)
        MyList.pop(MyList.index(min_num))
        i = i + 1 
    return sorted_List
    
# getting list from input
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
my_list = list_create()
result = List_Sorting(my_list)
print(result)

################### Sample Solution ###################
def _custom_bubble_sort_sample_(original_list):
    # This is an implementation of the
    # famous bubble sort algorithm
    # This can a very inefficient algorithm
    # when used with large data
         
    # our purpose here however is to show how to sort
    # a list without any built-in methods
	

    # make a copy of the original list
    my_list = original_list[:]
  
    # get the length of the list
    length = 0
    for element in my_list:
        length = length + 1
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, length-1):
            # if next element is greater element then swap them
            if my_list[index] > my_list[index + 1]:
                temporary_variable = my_list[index]
                my_list[index] = my_list[index + 1]
                my_list[index + 1] = temporary_variable
                unSorted = True
    return my_list