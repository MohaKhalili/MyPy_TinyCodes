def odd_number(n):

sum_n = 0

for i in range(0,n+1):
    if n[i] % 2 != 0:
        sum_n = sum_n + n[i]

return sum_n
