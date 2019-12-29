# a function that takes a two-dimensional list (list of lists) of numbers
# as argument and returns a list which includes the sum of each row.
def List_of_Sum_of_Rows_of_2D_List(my_list):
    total = 0
    sum_list = []
    for dim2 in my_list:
        for index in range(len(dim2)):
            total = total + dim2[index]
        sum_list.append(total)
        total = 0
    return sum_list

# driver code tester
my_list = [[1,5],[3,7]]
result = List_of_Sum_of_Rows_of_2D_List(my_list)
print(result)