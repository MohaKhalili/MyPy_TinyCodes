# A function named test_for_anagrams that receives two strings as parameters, 
# both of which consist of alphabetic characters and returns True if the two 
# strings are anagrams, False otherwise. Two strings are anagrams if one string 
# can be constructed by rearranging the characters in the other string using all 
# the characters in the original string exactly once. For example, the strings 
# "Orchestra" and "Carthorse" are anagrams because each one can be constructed 
# by rearranging the characters in the other one using all the characters in one 
# of them exactly once. Note that capitalization does not matter here i.e. a lower 
# case character can be considered the same as an upper case character.

# Type your code here
def test_for_anagrams(my_string1, my_string2):
    my_string1 = my_string1.lower().replace("", " ").split()
    my_string2 = my_string2.lower().replace("", " ").split()
    if sorted(my_string1) == sorted(my_string2):
        return True
    else:
        return False

# driver code tester
String1 = input("Please enter your string : ")
String2 = input("Please enter your string : ")
result = test_for_anagrams(String1, String2)
print(result)

################### Instructor function ###################
# def _are_anagrams_sample_(sample_string1, sample_string2):
#     if sorted(sample_string1.lower()) == sorted(sample_string2.lower()):
#         return True
#     else:
#         return False