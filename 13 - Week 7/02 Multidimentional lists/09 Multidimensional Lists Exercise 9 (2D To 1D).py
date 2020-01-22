# A function that accepts a 2-dimensional list of integers, and 
# returns a sorted (ascending order) 1-Dimensional list containing 
# all the integers from the original 2-dimensional list.

def D2_To_D1(my_list):
    output_list = []
    for item in my_list:
        for element in item:
            output_list.append(element)
    return sorted(output_list)

# driver code tester
my_list = [[10, 2, 3, 4], [2, 4, 0, 8]]
result = D2_To_D1(my_list)
print(result)