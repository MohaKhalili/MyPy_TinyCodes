# A function that accepts a number as argument and returns the square of the number. 

def get_var(k):
    result = k ** 2
    return result

# Driver code test
number = int(input("Please enter the number : "))
result = get_var(number)
print(result)