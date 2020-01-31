# A function named row_maximums that accepts a 2-dimensional list of numbers as 
# parameter and returns a dictionary whose values would be the maximum value of 
# each row and whose keys would be the appropriate strings as specified below.

# For example if the function receives the following list:
# [[5, 0, 0, 0, 13],
#  [0, 12, 0, 0],
#  [20, 0, 11, 0],
#   [6, 0, 0, 8]]

# then your function should return the dictionary such as:
# {'row 0 max': 13, 'row 1 max': 12, 'row 3 max': 8, 'row 2 max': 20}

# Notes:

#     Everything in the keys is separated by one space and the characters are lower cased.
#     The 2-dimensional list may have different number of columns in each row.
#     The row indicies for the keys should start at 0 and go to n. So your program should 
#     work for any number of rows and columns.
#     You may not use the built in max() function. 

# Type your code here
def row_maximums(some_multi_dimensional_list):
    output_dict = {}
    for i in range(len(some_multi_dimensional_list)):
        max_row = some_multi_dimensional_list[i][0]
        for j in range(1, len(some_multi_dimensional_list[i])):
            if some_multi_dimensional_list[i][j] > max_row:
                max_row = some_multi_dimensional_list[i][j]
        out_key = 'row ' + str(i) + ' max'
        output_dict[out_key] = max_row
    return output_dict            

# driver code test
my_list = [[5, 0, 0, 0, 13],
            [0, 12, 0, 0],
            [20, 0, 11, 0],
            [6, 0, 0, 8]]
result = row_maximums(my_list)
print(result)

################### Instructor function ###################
def _max_of_each_row_sample_q5(my_multidimensional_list):
    def calculate_my_max(some_list):
        sample_max = some_list[0]
        for number in some_list:
            if number >= sample_max:
                sample_max = number

        return sample_max

    list_of_max = []
    for rows in my_multidimensional_list:
        my_max = calculate_my_max(rows)
        list_of_max.append(my_max)
    #my_sorted_list = sorted(list_of_max)
    my_dict = {}
    for x in range(0, len(list_of_max)):
        my_string = 'row' + " " +  str(x) + " " + 'max'
        my_dict[my_string] = list_of_max[x]
    
    return my_dict