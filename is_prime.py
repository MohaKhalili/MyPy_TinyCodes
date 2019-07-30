# Type your code here
def is_prime(n):
    is_prime = True
    if n <= 1:
        is_prime = False   
    for counter in range(2,n):
        if n % counter == 0:
            is_prime = False
    return is_prime
