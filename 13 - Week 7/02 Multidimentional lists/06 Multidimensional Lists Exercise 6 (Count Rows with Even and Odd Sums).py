# A function that will receive a 2D list of integers. 
# The function should return the count of how many rows of 
# the list have even sums and the count of how many rows 
# have odd sums. For example if the even count was 2, and 
# odd count was 4 your function should return them in a list 
# like this: [2, 4].

# Type your code here
def Count_Rows_with_Even_and_Odd_Sums(my_list):
    even_count = 0
    odd_count = 0
    for item in my_list:
        sum_num = 0
        for element in item:
            sum_num += element
        if sum_num % 2 == 0 :
            even_count += 1
        else:
            odd_count += 1
    return [even_count, odd_count]

# driver code tester
my_list = [[1, 2, 3, 5], [5, -6, -9, 9], [2, 2, 2, 2], [1, 1, 1, 0]]
result = Count_Rows_with_Even_and_Odd_Sums(my_list)
print(result)