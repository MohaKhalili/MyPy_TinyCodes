# A function that accepts a list as input and returns a new list 
# which includes every other element in the original list. Keep 
# the first element, i.e. input_list[0]. For example if:

# input_list = ["we", "love", "python", "so","much"]

# then your function should return a list such as:

# ['we', 'python', 'much']

# method 1
def Every_Other_Element1(MyList):
    MyNewList = []
    for i in range(0,len(MyList),2):
        MyNewList.append(MyList[i])
    return MyNewList

# method 2    
def Every_Other_Element2(list):
    my_list = []
    for i in range(len(list)):
        if i % 2 == 0:
            my_list.append(list[i])
    return my_list

# this is a function for getting list by input
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
result = Every_Other_Element(my_list)
print(result)