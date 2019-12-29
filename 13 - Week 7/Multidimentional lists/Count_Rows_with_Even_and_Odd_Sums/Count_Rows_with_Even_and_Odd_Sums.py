# a function that will receive a 2D list of integers. The function should
# return the count of how many rows of the list have even sums and the
# count of how many rows have odd sums.
def Count_Rows_with_Even_and_Odd_Sums(my_list):
    count_odd = 0
    count_even = 0
    for dim2 in my_list:
        total = 0
        for index in range(len(dim2)):
            total = total + dim2[index]
        if (total % 2) == 0:
            count_even = count_even + 1
        elif (total % 2 != 0):
            count_odd = count_odd + 1
    result = [count_even, count_odd]
    return result

# driver code tester
my_list = [[3,6],[2,9]]
result = Count_Rows_with_Even_and_Odd_Sums(my_list)
print(result)