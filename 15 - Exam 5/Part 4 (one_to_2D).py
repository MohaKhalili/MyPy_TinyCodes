# A function named one_to_2D which receives an input list and two integers r and c as 
# parameters and returns a new two-dimensional list having r rows and c columns.

# Note that if the number of elements in the input list is larger than r*c then ignore 
# the extra elements. If the number of elements in the input list is less than r*c then 
# fill the two dimensional list with the keyword None. For example if your fuction is 
# called as hown below:

# one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3)
# Then it should return:
# [[8, 2, 9],[4, 1, 6]]

################### My function ###################
def one_to_2D(some_list, r, c):
    out_2D = list()
    m = 0
    for i in range(r):
        out_2D.append([])
        for j in range(c):
            out_2D[i].append(some_list[m] if m < len(some_list) else None)
            m += 1
    return out_2D

# ################### driver code tester ###################
some_list = [1, 2, 3, 4]
row = 3
col = 4
result = one_to_2D(some_list, row, col)
print(result)

################### Instructor function ###################
def _1d_to_2d_sample_(sample_list, rows, cols):
    my_2d_list = []
    product = rows * cols
    length = len(sample_list)
    if length > product:
        # ignore the extra elements by slicing
        # and creating a new list to work with
        sample_list = sample_list[0:product]
    else:
        # fill the rest of the index of the
        # 2d list with None
        difference = product - length
        for i in range(length, length+difference):
            sample_list.append(None)

    for i in range(0, len(sample_list), cols):
        my_2d_list.append(sample_list[i:i+cols])

    return my_2d_list