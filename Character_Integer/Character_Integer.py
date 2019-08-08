# a function that accepts an alphabetic character and returns
# the number associated with it from the ASCII table. 
def Character_Integer(ch):
    integer = ord(ch)
    return integer

# driver test code
n = input ("please enter an character: ")
result = Character_Integer(n)
print (result)