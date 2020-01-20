# A function that accepts a 2 Dimensional list of integers and returns the average. 
# Remember that average = (sum_of_all_items) / (total_number_of_items). 

# Type your code here
def Average_of_2D_List(my_list):
    total_num = 0
    counter = 0
    for item in my_list:
        for num in item:
            total_num += num
            counter += 1
    average = total_num / counter
    return average

# driver code tester
my_list = [[3, 5],[6, 8]]
result = Average_of_2D_List(my_list)
print(result)