# A function that accepts two (matrices) 2 dimensional lists 
# a and b of unknown lengths and returns True if they can be 
# multiplied together False otherwise. Hint: Two matrices a 
# and b can be multiplied together only if the number of 
# columns of the first matrix(a) is the same as the number 
# of rows of the second matrix(b). The input for this function 
# will be two 2 Dimensional lists. For example if the input 
# lists are:

# a = [[2, 3, 4],
#      [3, 4, 5]]
# b = [[4, -3, 12],
#      [1, 1, 5],
#      [1, 3, 2]]

# Then your function should return a boolean value:
#  True

def Multiplication_Check_two_Matrices(list1, list2):
    if len(list1[0]) == len(list2):
        return True
    else:
        return False
    
# driver code tester
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
result = Multiplication_Check_two_Matrices(a, b)
print(result)