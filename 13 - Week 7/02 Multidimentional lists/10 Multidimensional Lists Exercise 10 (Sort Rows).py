# A function that accepts a 2-dimensional list of integers, and 
# sorts (descending order) all the elements inside each row and 
# returns the sorted 2-dimensional list.

def Sort_Rows(my_list):
    output_list = []
    for item in my_list:
        new_item = []
        new_item = sorted(item, reverse=True)
        output_list.append(new_item)
    return output_list

# driver code tester
my_list = [[10, 2, 3, 4], [2, 4, 0, 8]]
result = Sort_Rows(my_list)
print(result)

################### Sample Solution ###################
# def _2d_rows_sorted_sample_(_2d_list):
#     for rows in _2d_list:
#         rows.sort(reverse=True)
#     return _2d_list