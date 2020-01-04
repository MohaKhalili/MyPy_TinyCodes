# A function which accepts an input string consisting of alphabetic characters 
# and spaces and returns the string with all the spaces removed. Do NOT use any 
# string methods for this problem.

# method 1
def Remove_All_Spaces(input_str):
    new_str = ""
    for chara in input_str:
        if ord(chara) == ord(" "):
            continue
        else:
            new_str += chara
    return new_str

# method 2
def Remove_All_Spaces(my_str):
    new_str = ""
    for i in range(len(my_str)):
        if ord(my_str[i]) != " ":
            new_str = new_str + chr(ord(my_str[i]))
    return new_str

# Driver code tester
my_str = input("Please enter your string : ")
result = Remove_All_Spaces(my_str)
print(result)