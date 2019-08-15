#  a function that takes a string consisting of alphabetic
#  characters as input argument and returns True if the
#  string is a palindrome. A palindrome is a string which
#  is the same backward or forward.
def StringIsPalindrome(Str):
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

#driver code test
String = "AasdfgFDSAA"
result = StringIsPalindrome(String)
print(result)