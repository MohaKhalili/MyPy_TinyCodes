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

# An example of the input file is shown below. Sample Input Output Assuming that the input file "student_grades.txt" contains the following text:

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


# Type your code here
def create_grades_dict(file_name):
    my_file = open(file_name,'r')
    data = my_file.readlines()
    my_file.close()
    
    out_dict = {}

    for line in data:
        line = line.strip().replace(" ","").split(',')
        index = int((len(line) - 2) / 2)
        list_test = []

        for index in range(len(line)):
            if index == 0:
                list_test.append(line[1])
                out_dict[line[0]] = list_test
            elif index == 1:
                continue
            elif index % 2 == 1:
                list_test.append(int(line[index]))
                out_dict[line[0]] = list_test
    return out_dict



################### Driver Code Tester ###################
file_directory = '.\\17 - Assignment 4\\student_grades.txt'
result = create_grades_dict(file_directory)
print(result)