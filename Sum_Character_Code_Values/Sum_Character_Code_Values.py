# a function that accepts an alphabetic string and returns
# an integer which is the sum of all the UTF-8 codes of 
# the character in that string. 
def Sum_Character_Code_Values(input_string):
    sum_str = 0
    for i in input_string:
        sum_str = sum_str + ord(i)
    return sum_str


# driver test code
n = input("please enter the string: ")
result = Sum_Character_Code_Values(n)
print(result)