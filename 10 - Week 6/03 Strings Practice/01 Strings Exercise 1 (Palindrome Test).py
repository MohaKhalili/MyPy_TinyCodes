# A function that takes a string consisting of alphabetic characters as input 
# argument and returns True if the string is a palindrome. A palindrome is a 
# string which is the same backward or forward. Note that capitalization does 
# not matter here i.e. a lower case character can be considered the same as an 
# upper case character.

# method 1
def StringIsPalindrome1(Str):
    Str = Str.lower()
    IsPalindrome = True
    for i in range(len(Str)):
        if Str[i] != Str[-i-1]:
            IsPalindrome = False
    return IsPalindrome

# method 2
def StringIsPalindrome2(Str):
    result = True
    for i in range(len(Str)):
        if Str[i].isupper():
            if (chr(ord(Str[i])) != chr(ord(Str[-1-i]))) and (chr(ord(Str[i])) != chr(ord(Str[-1-i])-32)):
                result = False
                break
        elif Str[i].islower():
            if (chr(ord(Str[i])) != chr(ord(Str[-1-i]))) and (chr(ord(Str[i])) != chr(ord(Str[-1-i])+32)):
                result = False
                break
    return result

# Driver code test
input_str = input("Please enter your string : ")
result = StringIsPalindrome1(input_str)
print(result)

################### Sample Solution ###################
def _is_palindrome_sample_(sample_string):
    # Check if the inverted string  equals the original string
    if str(sample_string).lower() == str(sample_string)[::-1].lower():
        return True     # Sample string is a palindrome
    else:
        return False    # Sample string is not a palindrome