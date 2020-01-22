# A function that accepts two (matrices) 2 dimensional lists 
# a and b of unknown lengths and returns their product. Hint: 
# o matrices a and b can be multiplied together only if the 
# number of columns of the first matrix(a) is the same as the 
# ber of rows of the second matrix(b). Hint: You may import 
# and use the numpy module but your return must be a python 
# list not a numpy array. The input for this function will 
# be two 2 Dimensional lists. For example if the input lists 
# are:

# a = [[2, 3, 4],
#      [3, 4, 5]]
# b = [[4, -3, 12],
#      [1, 1, 5],
#      [1, 3, 2]]

# Then your function should return their product such as:

# [[15, 9, 47], [21, 10, 66]] 

def Multiplication_two_Matrices(Mat1, Mat2):
    import numpy
    product = (numpy.mat(Mat1) * numpy.mat(Mat2))
    product_to_list = product.tolist()
    return product_to_list

# driver code tester
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

result = Multiplication_two_Matrices(a, b)
print(result)