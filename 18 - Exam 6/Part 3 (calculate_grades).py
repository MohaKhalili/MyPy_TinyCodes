# A function named calculate_grades that receives a file name. 
# The file contains names of students and their grades for 4 
# quizzes and returns a tuple as specified below. 

# Each line of the file will have the following format:
# name,quiz1_score,quiz2_score,quiz3_score,quiz4_score

# For example if the contents of the file are:
# john,89,94,81,97
# eva,40,45,65,90
# joseph,0,0,54,99
# tim,73,74,89,91

# The name and grades are separated by commas. Your function 
# should return the names of the student and their quiz averages 
# as a tuple of tuples as shown below:

# (('eva', 60.0), ('john', 90.25), ('joseph', 38.25), ('tim', 81.75))

# The tuples should be sorted in ascending order by the student's name.

################### My Solution ###################
def calculate_grades(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    out_list = []
    for item in data:
        item = item.strip().split(',')
        name, garde1, grade2, grade3, grade4 = [item[0], int(item[1]), int(item[2]), int(item[3]), int(item[4])]
        Avg = (garde1 + grade2 + grade3 + grade4) / 4
        test_tuple = tuple([name, Avg])
        out_list.append(test_tuple)
    return tuple(sorted(out_list))


################### Driver Code ###################
file_directory = '.\\18 - Exam 6\\Part3 (calculate_grades).csv'
result = calculate_grades(file_directory)
print(result)

################### Sample Solution ###################
def sample_quiz6_grades_sample(file_name):
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    students_list = []
    for each_line in data:
        name,quiz1,quiz2,quiz3,quiz4 = each_line.strip().split(',')
        quiz_average = (float(quiz1)+float(quiz2)+float(quiz3)+float(quiz4))/4
        students_list.append((name,quiz_average))
    
    
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, len(students_list)-1):
            # if next element is greater element then swap them
            if students_list[index][0] > students_list[index + 1][0]:
                temporary_variable = students_list[index]
                students_list[index] = students_list[index + 1]
                students_list[index + 1] = temporary_variable
                unSorted = True    
    my_tuple = tuple(students_list)
    return my_tuple