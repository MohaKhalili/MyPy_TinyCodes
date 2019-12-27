# A function that accepts two lists both of which contain integers and 
# returns a new list which contains all the elements from both lists 
# sorted in descending order. Your new list should include duplicate 
# elements if they exist. Do NOT use the built in sort() or sorted() 
# methods.

# method 1
def Extending_Sorting(my_list1, my_list2):
    one_list = my_list1 + my_list2
    i = len(one_list)
    output = []
    while i != 0:
        output.append(max(one_list))
        one_list.pop(one_list.index(max(one_list)))
        i = i - 1
    return output

# method 2
def Extending_Sorting(List1, List2):
    List1.extend(List2)
    def sorting_list(MyList):
        sorted_List = []
        i = 0
        while len(MyList) > 0 :
            max_num = MyList[0]
            for j in range(len(MyList)):
                if max_num < MyList[j]:
                    max_num = MyList[j]
            sorted_List.insert(i,max_num)
            MyList.pop(MyList.index(max_num))
            i = i + 1 
        return sorted_List

    result = sorting_list(List1)
    return result

# getting list 1 from input
def list_create1():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of list 1 elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter the list 1 element : "))
  
        lst.append(ele) # adding the element
    return lst 

# getting list 2 from input
def list_create2():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of list 2 elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter the list 2 element : "))
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list1 = list_create1()
my_list2 = list_create2()
result = Extending_Sorting(my_list1, my_list2)
print(result)

################### Sample Solution ###################
# def _merge_and_sort_sample_(a, b):
#     a.extend(b)
#     # Create a new list
#     new_list = []
#     # Loop until a becomes empty
#     while a:
#         # set an arbitrary element as the minimum
#         # in this case we chose the first index
#         maximum = a[0]
#         # loop through the list and
#         # find the element that is smallest
#         for element in a:
#             if element > maximum:
#                 maximum = element
#         # append the smallest element to the new list
#         new_list.append(maximum)
#         # now remove that smallest element from the original list
#         a.remove(maximum)
#     # Ultimately a will become empty
#     # and the loop will end
#     # now return the new list
#     return new_list