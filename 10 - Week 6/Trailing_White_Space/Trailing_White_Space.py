# a function that accepts an input string consisting of alphabetic characters
# and removes all the trailing whitespace of the string and returns it without
# using any .strip() method.

def Trailing_White_Space(str):
    index = []
    for i in range(len(str)-1,0,-1):
        if str[i] != " ":
            index = i + 1
            break
    str_new = str[:index]
    return str_new

# driver code
x = "*   hello         "
y = Trailing_White_Space(x)
print(y)