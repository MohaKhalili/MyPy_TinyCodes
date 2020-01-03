# A function that accepts an alphabetic character and returns the 
# number associated with it from the ASCII table.

# Type your code here
def Character_Integer(ch):
    integer = ord(ch)
    return integer

# Driver code test
n = input("Please enter your character : ")
result = Character_Integer(n)
print(result)