# A function that takes a two-dimensional list (list of lists) of 
# numbers as argument and returns a list which includes the maximum 
# value of each column. Assume that the length of columns is consistent 
# in each row. 

def List_Column_Maximums(my_list):
    output_list = []
    for i in range(len(my_list[0])):
        test_list = []
        for item in my_list:
            test_list.append(item[i])
        output_list.append(max(test_list))
    return output_list

# driver code tester
my_list = [[10, 2, 3, 4], [2, 4, 0, 8]]
result = List_Column_Maximums(my_list)
print(result)

################### Sample Solution ###################
# def _max_of_columns_sample_(sample_list):
#     cols = len(sample_list[0])
#     mylist = []
#     for c in range(cols):
#         column_max = 0
#         for row in sample_list:
#             if row[c] > column_max:
#                 column_max = row[c]
#         mylist.append(column_max)
#     return mylist