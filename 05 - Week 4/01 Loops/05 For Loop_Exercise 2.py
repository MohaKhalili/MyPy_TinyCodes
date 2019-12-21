# A program which asks the user to type an integer, n, and then 
# prints the sum of all numbers from 1 to n (including both 1 and n).

# Type your code here

n = input('please enter your number : ')
n = int(n)
n_sum = 0
for N in range(1,n+1):
    n_sum = n_sum + N
print(n_sum)