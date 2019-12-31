# A function named list_of_primes that accepts a positive integer n 
# and returns a sorted list (ascending order) of all the prime numbers
# between 2 and n (including 2 but not including n)

# Type your code here
def list_of_primes(n):
    PrimeList = []
    for i in range(2,n):
        Condition = True
        for count in range(2,i):
            if i % count == 0:
                Condition = False
        if Condition:    
            PrimeList.append(i)
    return PrimeList

# Driver code test
n = int(input("Please enter the integer number : "))
result = list_of_primes(n)
print("The prime numbers between 2 and", n, "is :", result)

################### Instructor function ###################
# def _list_of_primes_sample_(n):
#     my_list = []
#     integer = 2
#     while integer < n:
#         prime = True
#         start = 2
#         while start < integer:
#             if integer % start == 0:
#                 prime = False
#             start = start + 1
#         if prime == True:
#             my_list.append(integer)
#         integer = integer + 1
#     return my_list