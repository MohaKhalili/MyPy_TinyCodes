# A function named multiplication_table that receives a positive integer 'n' as parameter
# and returns a n by n multiplication table as a two-dimensional list.

# For example if the integer received by the function 'n' is:
# 4
# then your program should return a two_dimensional list with 4 rows and 4 columns such as:
# [[1, 2, 3, 4],
#  [2, 4, 6, 8],
#  [3, 6, 9, 12],
#  [4, 8, 12, 16]]

################### My function ###################
def multiplication_table(n):
    output_table = []
    for i in range(1, n+1):
        output_table.append([])
        for j in range(1, n+1):
            output_table[i-1].append(j*i)
    return output_table

################### Driver code test ###################
number = int(input("Please enter your number : "))
result = multiplication_table(number)
print(result)

################### Instructor function ###################
def _multiplication_table_sample_q5(n):
    total_list = []
    for r in range(1, n+1):
        for c in range(1, n+1):
            total_list.append(r*c)
    multiplication_table = []
    for i in range(0, len(total_list), n):
        multiplication_table.append(total_list[i:i+n])
    return multiplication_table