# a function named single_insert_or_delete that accepts
# two strings as input arguments and returns:
#
#     0     if the two strings match exactly.
#     1     if the first string can become the same as the second
#           string by inserting or deleting a single character.
#           Notice that inserting and deleting a character is not
#           the same as replacing a character.
#     2     otherwise

def single_insert_or_delete(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    result = 0
    if s1 != s2:
        if len(s1) != len(s2):
            result = 2
            max_string = max(s1, s2)
            for index in range(min(len(s1), len(s2))):
                if s1[index] != s2[index]:
                    max_string = max_string.replace(max_string[index],"",1)
                    if max_string == min(s1, s2):
                        result = 1
                        break
                elif max_string.replace(max_string[-1],"",1) == min(s1, s2):
                    result = 1
        else:
            result = 2
    return result

# driver code test
input_string1 = input("enter your first string: ")
input_string2 = input("enter your second string: ")
result = single_insert_or_delete(input_string1, input_string2)
print(result)