# A function that accepts an alphabetic string and returns an integer 
# which is the sum of all the UTF-8 codes of the character in that string. 
# For example if the input string is "hello" then your function should return 532

def Sum_Character_Code_Values(my_str):
    sum_num = 0
    for my_char in my_str:
        sum_num += ord(my_char)
    return sum_num

# Driver code test
n = input("Please enter your string : ")
result = Sum_Character_Code_Values(n)
print(result)