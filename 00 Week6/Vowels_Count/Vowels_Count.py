# a function which returns the total number of vowels in
# an input string which consists of alphabetic characters.
# Note that capitalization does not matter here i.e. a lower
# case character should be considered the same as an upper case
# character. For this problem.
# The vowels are considered to be A, E, I, O, U.

def Vowels_Count(String):
    count = 0
    vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for my_char in String:
        for list_char in vowels_list:
            if my_char == list_char:
                count = count + 1
    return count

# driver code test
String = "hello mohammad"
result = Vowels_Count(String)
print(result)