# a function that accepts a string and a character as
# input and returns the number of times the character
# is repeated in the string. Note that capitalization
# does not matter here i.e. a lower case character
# should be treated the same as an upper case character.

def Count_Input_Character(String,char):
    String = String.upper()
    char = char.upper()
    count = 0
    for i in String:
        if i == char:
            count = count + 1
    return count

# driver code test
String = "mohammad hello"
char = "m"
result = Count_Input_Character(String,char)
print(result)