# A function that accepts two positive integers a and b 
# (a is smaller than b) and returns a list that contains
#  all the odd numbers between a and b (including a and 
# including b if applicable) in descending order. 

def odd_numbers_list(num1, num2):
    list = []
    for i in range(num1, num2+1):
        if i % 2:
            list.append(i)
    list.reverse()
    return list

# Driver code test
number1 = int(input("Please enter the first number : "))
number2 = int(input("Please enter the second number : "))
result = odd_numbers_list(number1, number2)
print(result)