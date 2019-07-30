# print all prime numbers between 2 and 50

for this_number in range(2,51):
    is_prime = True
    for counter in range(2,this_number):
        if (this_number%counter == 0):
            is_prime = False
            break

    if(is_prime): # yani agar True monde bud
        print(this_number)
