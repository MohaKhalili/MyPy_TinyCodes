#  a function that accepts an input string consisting of alphabetic
#  characters and removes all the leading whitespace of the string
#  and returns it without using .strip().
def Leading_White_Space(str):
    index = []
    for i in range(len(str)):
        if str[i] != " ":
            index = i
            break
    str_new = str[index:]
    return str_new

# driver code
x = "   hello         *"
y = Leading_White_Space(x)
print(y)