# A program which asks the user to type a positive integer, n, and 
# then prints the sum of the square of all numbers form 1 to n (including both 1 and n).

# For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14 

# Type your code here

n = input('please enter your number : ')
n = int(n)
sum_N = 0
for N in range(1,n+1):
    sum_N = sum_N + (N**2)
print(sum_N)