# a function that takes a two-dimensional list (list of lists) of numbers
# as argument and returns a list which includes the maximum value of each row.
def List_of_Row_Maximums(my_list):
    result = []
    for dim2 in my_list:
        max_number = dim2[0]
        for index in range(1, len(dim2)):
            if max_number <= dim2[index]:
                max_number = dim2[index]
        result.append(max_number)
    return result

# driver code tester
my_list = [[3, 6, 6.25], [-10, 10, 100]]
result = List_of_Row_Maximums(my_list)
print(result)