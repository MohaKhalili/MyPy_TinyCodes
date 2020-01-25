# A function that takes a string as input argument and returns a dictionary of 
# vowel counts i.e. the keys of this dictionary should be individual vowels and 
# the values should be the total count of those vowels. You should ignore white 
# spaces and they should not be counted as a character. Also note that a small 
# letter vowel is equal to a capital letter vowel.

def Dictionary_of_Vowel_Count(my_string):
    my_string = my_string.lower().replace(" ","")
    output_dict = {}
    for chara in my_string:
        if chara in ['a', 'e', 'i', 'o', 'u']:
            output_dict[chara] = output_dict.get(chara, 0) + 1
    return output_dict

# driver code tester
string = input("Please enter your string : ")
result = Dictionary_of_Vowel_Count(string)
print(result)

################### Sample Solution ###################
# def _dictionary_of_vowel_counts_sample_(sample_string):
#     stripped_string = sample_string.replace(" ", "")        # remove all white spaces
#     lowercase_stripped_string = stripped_string.lower()     # convert to lower case
#     sample_dictionary = {}
#     vowels = ["a", "e", "i", "o", "u"]
#     # Iterate through the given string and set each 
#     # character as a key and its count as the value
#     for character in lowercase_stripped_string:
#         if character in vowels:
#             sample_dictionary[character] = sample_string.count(character)
#     return sample_dictionary