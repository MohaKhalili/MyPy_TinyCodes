# A function that takes a two-dimensional list (list of lists) 
# of numbers as argument and returns a list which includes the 
# sum of each column. Assume that the number of columns in each 
# row is the same.

# Type your code here
def List_of_Sum_of_Columns_of_2D_List(my_list):
    sum_num = 0
    output_list = []
    for i in range(len(my_list[0])):
        for item in my_list:
            sum_num += item[i]
        output_list.append(sum_num)
        sum_num = 0
    return output_list

# driver code tester
my_list = [[3, 5],[6, 8]]
result = List_of_Sum_of_Columns_of_2D_List(my_list)
print(result)