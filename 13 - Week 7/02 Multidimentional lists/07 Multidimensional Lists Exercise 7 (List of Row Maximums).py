# A function that takes a two-dimensional list (list of lists) 
# of numbers as argument and returns a list which includes the 
# maximum value of each row.

# Type your code here
def List_of_Row_Maximums(my_list):
    output_list = []
    for item in my_list:
        max_num = item[0]
        for element in item:
            if element > max_num:
                max_num = element
        output_list.append(max_num)
    return output_list

# driver code tester
my_list = [[3, 5],[6, 8]]
result = List_of_Row_Maximums(my_list)
print(result)

################### Sample Solution ###################
# def _max_of_rows_sample_(sample_list):
#     mylist = []
#     for item in sample_list:
#         mylist.append(max(item))
#     return mylist