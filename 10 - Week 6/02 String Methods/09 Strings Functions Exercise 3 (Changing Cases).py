# A function which accepts an input string and returns a string where the 
# case of the characters are changed, i.e. all the uppercase characters are 
# changed to lower case and all the lower case characters are changed to 
# upper case. The non-alphabetic characters should not be changed. Do NOT 
# use the string methods upper(), lower(), or swap(). 

# Type your code here
def Changing_Cases(input_str):
    new_str = ''
    for chara in input_str:
        if ord(chara) >= 65 and ord(chara) <= 90:
            new_str += chr(ord(chara)+32)
        elif ord(chara) >= 97 and ord(chara) <= 122:
            new_str += chr(ord(chara)-32)
        else:
            new_str += chara
    return new_str

my_str = input("Please enter your string : ")
result = Changing_Cases(my_str)
print(result)