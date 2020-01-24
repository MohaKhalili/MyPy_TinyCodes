# A function that accepts a dictionary as input which contains the names 
# and grades of students (The keys are student names and the values are 
# lists of grades for 3 exams (1 Dimensional list)) and returns the list 
# of names for those students whose grade on all three exams is greater 
# than or equal to 78. 

# Type your code here
def Lists_as_Values(my_dict):
    dict_value = list(my_dict.values())
    dict_key = list(my_dict.keys())
    output_key = []
    for i in range(len(dict_value)):
        counter = 0
        for num in dict_value[i]:
            if num >= 78:
                counter += 1
        if counter == 3:
            output_key.append(dict_key[i])
    return output_key

# driver code tester
my_dict = {'James': [78,90,90], 'Tina': [20,15,10], 'Sam': [20,35,35]}
result = Lists_as_Values(my_dict)
print(result)

################### Sample Solution ###################
# def _dictionary_names_grades_sample_(sample_dictionary):
#     output_list = []
#     keys = sample_dictionary.keys()
#     for k in keys:
#         each_list = sample_dictionary[k]
#         grade1, grade2, grade3 = each_list[0], each_list[1], each_list[2]
#         if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
#             output_list.append(k)
#     return output_list