# A function that accepts a list (which has a length of 4 or more) and a 
# string and returns the list such that the second through the fourth 
# element (index 1 through 3 both inclusive) in the input list are 
# replaced by the input string. For example:

# input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
# input_string = "Brahman" 

# Then, your function should return a list such as:

# ['Isha', 'Brahman', 'Brahman', 'Brahman', 'Sri']

# method 1
def List_Updating(LIST, STR):
    for i in range(len(LIST)):
        if (i >= 1) and (i < 4):
            LIST[i] = STR
    return LIST

# method 2
def Updating_the_list(input_list,input_string):
    for i in range(1,4):
        input_list.pop(i)
        input_list.insert(i,input_string)
    return input_list

################### Sample Solution ###################
def _list_manipulation_sample1_(input_list, input_string):
    for i in range(1, 4):
        input_list[i] = input_string
    return input_list

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
str = input('please enter your string : ')
result = List_Updating(my_list, str)
print(result)