# A function named single_insert_or_delete that accepts two strings as input arguments and returns:
#
#     0     if the two strings match exactly.
#     1     if the first string can become the same as the second
#           string by inserting or deleting a single character.
#           Notice that inserting and deleting a character is not
#           the same as replacing a character.
#     2     otherwise

# method 1
def single_insert_or_delete1(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    len_string1 = len(string1)
    len_string2 = len(string2)
    if string1 == string2:
        return 0
    
    if abs(len_string1-len_string2)!=1:
        return 2

    if max(len_string1, len_string2) == min(len_string1, len_string2)+1:
        if len_string1 > len_string2:
            maximum_string = string1
            minimum_string = string2
        else:
            maximum_string = string2
            minimum_string = string1
        test_string = ''
        for i in range(len(maximum_string)):
            test_string = maximum_string.replace(maximum_string[i],'',1)
            if test_string == minimum_string:
                return 1
                break
            test_string = ''
        return 2

# method 2
def single_insert_or_delete2(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    result = 0
    if len(s1)>=len(s2):
        max_string = s1
        min_string = s2
    else:
        max_string = s2
        min_string = s1
    if s1 != s2:
        result = 2
        if len(s1) != len(s2):
            if (max_string.replace(max_string[-1], "", 1) == min_string) or (max_string.replace(max_string[0], "", 1) == min_string):
                result = 1
            for index in range(min(len(s1), len(s2) ) ):
                if s1[index] != s2[index]:
                    max_string = max_string.replace(max_string[index],"", 1)
                    if max_string == min_string:
                        result = 1
                        break
                    max_string = max(s1, s2)
    return result

# driver code test
input_string1 = input("enter your first string: ")
input_string2 = input("enter your second string: ")
result = single_insert_or_delete1(input_string1, input_string2)
print(result)

################### Instructor function ###################
def _instructor_function(s1,s2):
   s1=s1.lower()
   s2=s2.lower()
   if s1==s2:
       return 0
   if abs(len(s1)-len(s2))!=1:
       return 2

   if len(s1)>len(s2):
       # only deletion is possible
       for k in range(len(s2)):
           if s1[k]!=s2[k]:
               if s1[k+1:]==s2[k:]:
                   return 1
               else:
                   return 2
       return 1
   else: # s1 is shorter Only insertion is possible
       for k in range(len(s1)):
           if s1[k]!=s2[k]:
               if s1[k:]==s2[k+1:]:
                   return 1
               else:
                   return 2
       return 1