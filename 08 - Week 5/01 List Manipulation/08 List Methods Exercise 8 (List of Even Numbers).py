# A function that accepts two positive integers a and b and returns a 
# list of all the even numbers between a and b (including a and not including b).

def Even_numbers_list(num1, num2):
    list = []
    for i in range(num1, num2):
        if i % 2 == 0:
            list.append(i)
    return list

# Driver code test
number1 = int(input("Please enter the first number : "))
number2 = int(input("Please enter the second number : "))
result = Even_numbers_list(number1, number2)
print(result)