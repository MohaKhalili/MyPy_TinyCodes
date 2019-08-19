# a function that accepts a 2D list of integers and returns the maximum EVEN value
# for the entire list. You can assume that the number of columns in each row is the
# same. Your function should return None if the list is empty or all the numbers in
# the 2D list are odd.
def Maximum_Even_Value_of_2D_List(my_list):
    total = 0
    even_list = []
    for dim1 in my_list:
        for index in range(len(dim1)):
            test_number = dim1[index]%2
            if test_number == 0:
                even_list.append(dim1[index])
    if len(even_list) > 0:
        max_even = even_list[0]
        for i in range(1,len(even_list)):
            if max_even <= even_list[i]:
                max_even = even_list[i]
        result = max_even
    else:
        result = None
    return result

# driver code tester
my_list = [[3,5],[1,9]]
result = Maximum_Even_Value_of_2D_List(my_list)
print(result)