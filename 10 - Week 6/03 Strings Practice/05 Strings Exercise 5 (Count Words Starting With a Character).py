# A function that accepts a string and a character as input and returns 
# the count of all the words in the string which start with the given 
# character. Assume that capitalization does not matter here. You can 
# assume that the input string is a sentence i.e. words are separated 
# by spaces and consists of alphabetic characters.


def Count_Words_Starting_With_a_Character(String, chara):
    String = String.lower()
    String = String.split()
    counter = 0
    for item in String:
        if item[0] == chara.lower():
            counter += 1
    return counter

input_string = input("Please enter your string : ")
input_character = input("Please enter your character : ")
result = Count_Words_Starting_With_a_Character(input_string, input_character)
print(result)