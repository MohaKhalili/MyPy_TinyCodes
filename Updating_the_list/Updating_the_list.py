# Updating a List
# a function that accepts a list (which has a length of 4 or more) 
# and a string and returns the list such that the second through 
# the fourth element (index 1 through 3 both inclusive) in the 
# input list are replaced by the input string.

n = int(input("Enter number of elements (equal or more than 4 elements): ")) 
if n >=4:
    
    #getting the list
    input_list = []
    for i in range(0, n):
        print ("enter element index",i,": ",end = "")
        ele = input()
        input_list.append(ele) # adding the element 
    print("your list is: ",input_list) 

    #getting the string
    input_string = input("Please enter your string: ")

    #Updating list function
    def Updating_the_list(input_list,input_string):
        for i in range(1,4):
            input_list.pop(i)
            input_list.insert(i,input_string)
        return input_list

# driver test for my function
Updating_the_list(input_list,input_string)
print(input_list)