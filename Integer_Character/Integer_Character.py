# a function that accepts a positive integer n and 
# returns the ascii character associated with it.
def Integer_Character(n):
    character = chr(n)
    return character

# driver test code
n = int(input("please enter a number: "))
result = Integer_Character(n)
print(result)