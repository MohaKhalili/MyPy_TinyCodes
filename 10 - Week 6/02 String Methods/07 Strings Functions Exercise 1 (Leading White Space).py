# A function that accepts an input string consisting of alphabetic 
# characters and removes all the leading whitespace of the string 
# and returns it without using .strip(). For example if:

# input_string = "    Hello  "

# then your function should return a string such as:

# output_string = "Hello  "

# method 1
def Leading_White_Space1(my_str):
    for chara in my_str:
        if chara == " ":
            my_str = my_str.replace(chara,"",1)
        else:
            break
    return my_str

# method 2
def Leading_White_Space2(str):
    index = []
    for i in range(len(str)):
        if str[i] != " ":
            index = i
            break
    
    # slice the string from that index to the end
    str_new = str[index:]
    return str_new

my_str = input("Please enter your string : ")
result = Leading_White_Space1(my_str)
print(result)