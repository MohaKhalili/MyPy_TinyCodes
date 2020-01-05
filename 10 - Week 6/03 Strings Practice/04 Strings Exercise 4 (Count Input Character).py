# A function that accepts a string and a character as input and returns 
# the number of times the character is repeated in the string. Note that 
# capitalization does not matter here i.e. a lower case character should 
# be treated the same as an upper case character.

def Count_Input_Character(String, chara):
    String = String.upper()
    chara = chara.upper()
    counter = 0
    for item in String:
        if item == chara:
            counter += 1
    return counter

input_string = input("Please enter your string : ")
input_character = input("Please enter your character : ")
result = Count_Input_Character(input_string, input_character)
print(result)