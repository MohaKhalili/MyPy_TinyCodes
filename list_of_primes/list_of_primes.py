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

x = int(input("please enter a numbe, i will give you the prime numbers until that number :"))
x_prime_list = list_of_primes(x)
print(x_prime_list)