# A function that accepts three numbers and calculates their 
# product and returns the result.

# Type your code here
def Multiplying_Three_Numbers(first_num, second_num, third_number):
    result = first_num * second_num * third_number
    return result

# Driver code test
number1 = int(input("Please enter the first number : "))
number2 = int(input("Please enter the second number : "))
number3 = int(input("Please enter the third number : "))
result = Multiplying_Three_Numbers(number1,number2,number3)
print(result)