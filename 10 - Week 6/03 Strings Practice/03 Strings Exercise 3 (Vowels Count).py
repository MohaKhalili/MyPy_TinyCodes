# A function which returns the total number of vowels in an input string 
# which consists of alphabetic characters. Note that capitalization does 
# not matter here i.e. a lower case character should be considered the same 
# as an upper case character. For this problem, the vowels are considered 
# to be A, E, I, O, U.

def Vowels_Count(String):
    String = String.lower()
    vowels_list = ['a', 'i', 'o', 'e', 'u']
    count = 0
    for chara in String:
        if chara in vowels_list:
            count += 1
    return count

input_string = input("Please enter your string : ")
result = Vowels_Count(input_string)
print(result)