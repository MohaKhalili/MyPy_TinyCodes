# A function that takes a two-dimensional list (list of lists) 
# of numbers as argument and returns a list which includes the 
# sum of each row. You can assume that the number of columns in 
# each row is the same.

# Type your code here
def List_of_Sum_of_Rows_of_2D_List(my_list):
    output_list = []
    count_num = 0
    for item in my_list:
        for element in item:
            count_num += element
        output_list.append(count_num)
        count_num = 0
    return output_list

# driver code tester
my_list = [[3, 5],[6, 8]]
result = List_of_Sum_of_Rows_of_2D_List(my_list)
print(result)

################### Sample Solution ###################
# def _sum_of_rows_sample_(sample_list):
#     mylist = []
#     for item in sample_list:
#         mylist.append(sum(item))
#     return mylist