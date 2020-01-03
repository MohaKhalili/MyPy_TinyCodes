 # A function that accepts a positive integer n and returns the ascii 
 # character associated with it.

def Integer_Character(n):
    character = chr(n)
    return character

# Driver code test
n = int(input("Please enter your number : "))
result = Integer_Character(n)
print(result)