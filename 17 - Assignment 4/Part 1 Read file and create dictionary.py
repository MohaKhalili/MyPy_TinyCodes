# A function named create_grades_dict that accepts a string 
# as the name of a file. Assuming that the file is a text 
# file which includes name and grades of students, your 
# function should read the file and return a dictionary 
# with the exact format as shown below: The format of the 
# input file is:

# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
# .... 

# An example of the input file is shown below. Sample Input Output Assuming 
# that the input file "student_grades.txt" contains the following text:

# 1000123456, Rubble, Test_3,  80, Test_4 , 80
# 1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88

# Notes:

#     Items are seperated by comma and one or more spaces may exist between the items.
#     The "ID" of each student is unique. Two students may have the same Name 
#     (but IDs will be different)
#     The "Name" of each student will only include a last name with no punctuation. 
#     Maximum of 15 characters.
#     There will be an integer grade for each test (0-100)
#     There are only four valid tests, i.e. Test_1, Test_2, Test_3, Test_4. 
#     There may be other grades in the file and you should ignore those grades.
#     Each student may have missing grade(s) for the tests. A missing grades 
#     should be considered as 0.
#     Grades may not be in order i.e. Test_3 may appear before Test_1.

# Your function should read the input file, calculate the average test
# grade for each student and return a dictionary with the following format:
# {'Student_ID':[Last_name,Test_1_grade,Test_2_grade,Test_3_grade,Test_4_grade,average], ...}

# For example in the case of sample input file shown above, your function 
# should return the following dictionary:
# {'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}

################### My function ###################
# Type your code here
def create_grades_dict(file_name):
    my_file = open(file_name,'r')
    data = my_file.readlines()
    my_file.close()
    
    out_dict = {}

    for line in data:
        line = line.strip().replace(" ","").split(',')
        list_test = []
        flag_1, flag_2, flag_3, flag_4 = [0, 0, 0, 0]
        for index in range(len(line)):
            if index == 0:
                list_test.append(line[1])
                out_dict[line[0]] = list_test
            elif index == 1:
                continue
            else:
                if ('Test_1' in line) and (flag_1 == 0):
                    grade_1_index = line.index('Test_1') + 1
                    list_test.append(float(line[grade_1_index]))
                    flag_1 = 1
                elif ('Test_1' not in line) and (flag_1 == 0):
                    list_test.append(float(0))
                    flag_1 = 1
                elif ('Test_2' in line) and (flag_2 == 0):
                    grade_2_index = line.index('Test_2') + 1
                    list_test.append(float(line[grade_2_index]))
                    flag_2 = 1
                elif ('Test_2' not in line) and (flag_2 == 0):
                    list_test.append(float(0))
                    flag_2 = 1
                elif ('Test_3' in line) and (flag_3 == 0):
                    grade_3_index = line.index('Test_3') + 1
                    list_test.append(float(line[grade_3_index]))
                    flag_3 = 1
                elif ('Test_3' not in line) and (flag_3 == 0):
                    list_test.append(float(0))
                    flag_3 = 1
                elif ('Test_4' in line) and (flag_4 == 0):
                    grade_4_index = line.index('Test_4') + 1
                    list_test.append(float(line[grade_4_index]))
                    flag_4 = 1
                elif ('Test_4' not in line) and (flag_4 == 0):
                    list_test.append(float(0)) 
                    flag_4 = 1
        AVGERAGE = sum(list_test[1:]) / 4
        list_test.append(AVGERAGE)
    return out_dict

################### Driver Code Tester ###################
file_directory = '.\\17 - Assignment 4\\student_grades.txt'
result = create_grades_dict(file_directory)
print(result)

################### Instructor function ###################
# Type your code here
def _create_grades_dict(file_name):
    grade_dict={}
    tests=['Test_1','Test_2','Test_3','Test_4']
    fp=open(file_name,'r')
    lines=fp.readlines()
    fp.close()
    for line in lines:
        elements=line.strip().split(",")
        if elements and elements[0]:
            current_key=elements[0].strip()
            if len(current_key)==10:
                if grade_dict.get(current_key)==None:
                    # Key does not exist. Create it
                    grade_dict[current_key]=[elements[1].strip(),0,0,0,0,0]                
                for index in range(2,len(elements),2):
                    current_element=elements[index].strip()
                    if  current_element in tests:
                        grade_dict[current_key][int(current_element[-1])]=int(elements[index+1])
                grade_dict[current_key][5]=sum(grade_dict[current_key][1:5])/4.0
    return grade_dict