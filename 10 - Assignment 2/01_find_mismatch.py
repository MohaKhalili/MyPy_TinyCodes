# a function named find_mismatch that accepts
# two strings as input arguments and returns:
#       0   if the two strings match exactly.
#       1   if the two strings have the same length
#           and mismatch in only one character.
#       2   if the two strings do not have the same
#           length or mismatch in two or more characters.
from unittest import result


def find_mismatch(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        result = 2
    elif len(s1) == len(s2):
        count = 0
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                count = count + 1
        if count > 1:
            result = 2
        elif count == 1:
            result = 1
        else:
            result = 0
    return result

# driver code test
input_string1 = input("enter your first string: ")
input_string2 = input("enter your second string: ")
result = find_mismatch(input_string1, input_string2)
print(result)

################### Instructor function ###################
# def _instructor_function (s1,s2):
#    if len(s1) != len(s2):
#        return 2
#    s1=s1.lower()
#    s2=s2.lower()
#    number_of_mismatches=0
#    for index in range(len(s1)):
#        if s1[index] != s2[index]:
#            number_of_mismatches=number_of_mismatches+1
#            if number_of_mismatches>1:
#                return 2
#    return number_of_mismatches