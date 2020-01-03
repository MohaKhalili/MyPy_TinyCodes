# A function named find_gcd that accepts a list of positive integers 
# and returns their greatest common divisor (GCD). Your function should
# return 1 as the GCD if there are no common factors between the integers.

# Method 1
def find_gcd1(some_list):
    min_num = min(some_list)
    GCD_number = 1
    for i in range(2, min_num+1):
        condition_list = []
        for item in some_list:
            if item % i != 0:
                condition_list.append(False)
        if False not in condition_list:
            GCD_number = i
    return GCD_number

# Method 2
# Type your code here
def find_gcd2(my_list):     
    def Find_GCD_TwoNum(x, y): 
        while(y): 
            x, y = y, x % y 
        return x 
    num1 = my_list[0] 
    num2 = my_list[1]
    gcd = Find_GCD_TwoNum(num1, num2) 
    for i in range(2, len(my_list)): 
        gcd = Find_GCD_TwoNum(gcd, my_list[i])
    return gcd

def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter list element : ")) 
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = find_gcd1(my_list)
print(result)

 
################### Instructor function ###################
def sample_gcd_list_ed2_(my_list):
    result = my_list[0]
    for i in range(1, len(my_list)):
        result = my_gcd(result, my_list[i])
    return result
  
def my_gcd(a,b):
    while b:
        a, b = b, a%b
    return a