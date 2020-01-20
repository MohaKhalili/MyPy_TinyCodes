# A function which accepts a 2D list of numbers and returns the sum of all the number
# in the list You can assume that the number of columns in each row is the same.

# function
def Sum_of_2D_List(my_list):
    total_num = 0
    for item in my_list:
        for num in item:
            total_num += num
    return total_num

# driver code tester
my_list = [[3, 5],[6, 8]]
result = Sum_of_2D_List(my_list)
print(result)