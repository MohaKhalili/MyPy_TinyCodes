# Traversing Backwards
# a function that accepts a list and returns a new list such that the 
# new list contains all the items of the old list in reverse order. 

def Traversing_Backwards(input_list):
    new_list = []
    for i in range(0,len(input_list)):
        new_list.append(input_list[-1-i])
    return new_list

# driver test code
l = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']
result = Traversing_Backwards(l)
print(result)