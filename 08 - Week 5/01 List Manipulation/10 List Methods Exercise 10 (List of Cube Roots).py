# A function that accepts a positive integer k and returns the 
# ascending sorted list of cube root values of all the numbers 
# from 1 to k (including 1 and not including k). [if k is 1, your
# program should return an empty list]

def List_Cube_Roots(num):
    my_list = []
    for i in range(1,num):
        my_list.append(i**(1/3))
    my_list.reverse()
    return my_list

# Driver code test
number = int(input("Please enter the number : "))
result = List_Cube_Roots(number)
print(result)