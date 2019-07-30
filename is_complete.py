# Type your code here
def is_complete(n):
    is_complete = False
    sum_n = 0
    for counter in range(1,n):
        if n % counter == 0:
            sum_n = sum_n + counter
    if sum_n == n:
        is_complete = True
    return is_complete
