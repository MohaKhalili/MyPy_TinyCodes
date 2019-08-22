# a function which accepts a 2D list of numbers and returns the sum of all the number
# in the list You can assume that the number of columns in each row is the same.

def Sum_of_2D_List(my_list):
    total = 0
    for dim1 in my_list:
        for index in range(len(dim1)):
            total = total + dim1[index]
    return total

# driver code tester
my_list = [[3, 5],[6, 8]]
result = Sum_of_2D_List(my_list)
print(result)