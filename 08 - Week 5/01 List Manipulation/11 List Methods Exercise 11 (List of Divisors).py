# A function that accepts a positive integer k and returns the list of 
# all the divisors of k. Your list should include both 1 and k.

def List_of_Divisors(num):
    list = []
    for i in range(1, num+1):
        if num % i == 0:
            list.append(i)
    return list

# Driver code test
number = int(input("Please enter the number : "))
result = List_of_Divisors(number)
print(result)