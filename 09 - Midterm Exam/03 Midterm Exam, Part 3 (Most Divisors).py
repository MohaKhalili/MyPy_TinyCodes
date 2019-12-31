# A function called find_integer_with_most_divisors that accepts a list 
# of integers and returns the integer from the list that has the most 
# divisors. In case of a tie, return the first item that has the most 
# divisors. For example:

# if the list is:
# [8, 12, 18, 6]

# In this list, 8 has four divisors which are: [1,2,4,8] ; 12 has six 
# divisors which are: [1,2,3,4,6,12]; 18 has six divisors which are: 
# [1,2,3,6,9,18] ; and 6 has four divisors which are: [1,2,3,6]. Notice 
# that both 12 and 18 are tied for maximum number of divisors (both have 
# 6 divisors). Your function should return the first item with maximum 
# numer of divisors; so it should return: 12

# method 1
def find_integer_with_most_divisors_1(input_list):
    counter_list = []
    for item in input_list:
        counter = 0
        for j in range(1, item+1):
            if item % j == 0:
                counter = counter + 1
        counter_list.append(counter)
    most_divisors_index = counter_list.index(max(counter_list))
    Integer_with_most_divisors = input_list[most_divisors_index]
    return Integer_with_most_divisors

# method 2
def find_integer_with_most_divisors_2(input_list):
    def max_num_in_list( list ):
        max = list[ 0 ]
        for a in list:
           if a > max:
               max = a
        return list.index(max)
    CountList = []
    for i in input_list:
        count = 0
        Divisor = 1
        while Divisor <= i:
            if i % Divisor == 0:
                count = count + 1
            Divisor = Divisor + 1
        CountList.append(count)
    x = max_num_in_list(CountList) 
    return input_list[x]

# getting a list by input function
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Please enter the number of list element : "))
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("Enter the list element : ")) 
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = find_integer_with_most_divisors_1(my_list)
print("The integer with most divisors is : ", result)

################### Instructor function ###################
# def _integer_with_most_divisors_(sample_list):
#     # first set max_divisors to 0
#     max_divisors = 0
#     max_divisors_item = None
#     for items in sample_list:
#         # create a list to hold the divisors of all items in the list
#         output_list = []
#         for number in range(1, items):
#             # Check for the remainder when k is divided by number
#             # if the remainder is 0 that means number is a divisor of k
#             if items % number == 0:
#                 # append number to the output list
#                 output_list.append(number)
#         length = len(output_list)
#         # if the length of divisors for a particular element
#         # is greater than the current one i.e max_divisors
#         # then set max_divisors as that length and max_divisor_item as
#         # that particular item
#         if length > max_divisors:
#             max_divisors = length
#             max_divisors_item = items
#     return max_divisors_item