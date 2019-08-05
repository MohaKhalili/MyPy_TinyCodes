# Modifying a List
# a function that accepts a list that contains positive integers 
# and returns a new list which contains all the elements from 
# original list but adds 1 to those elements which are odd.
def Modifying_List(input_list):
    for i in range(len(input_list)):
        if input_list[i] % 2 != 0:
            input_list[i] = input_list[i] + 1
    return input_list

# driver test code for this function
l = [1,2,3,4,5,6,7,8,9]
e = Modifying_List(l)
print(e)