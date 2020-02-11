# A function called print_grades that accepts the name of a file (string) as input argument. 
# Assuming the format of the file is the same as the file in part 1, your function should 
# call the function that you developed in part 1 to read the file and create the grades 
# dictionary. Using the grades dictionary, your function should print the names, grades, 
# and averages of students with the exact format shown below. Notice that you are asked 
# to write a function (NOT a program) and that function prints the grades. Your function 
# should return None after printing the grades.

# Sample Input file:

# 1000123456, Rubble, Test_3,  80, Test_4 , 80, quiz , 90
# 1000123210, Bunny, Test_2, 100, Test_1, 100,Test_3   , 100 ,Test_4 , 100
# 1000123458, Duck, Test_1, 86, Test_5   , 100 , Test_2 ,93 ,Test_4, 94

# Your program's output should be:

#     ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |
# 1000123210 | Bunny            |    100 |    100 |    100 |    100 | 100.00 |
# 1000123456 | Rubble           |      0 |      0 |     80 |     80 |  40.00 |
# 1000123458 | Duck             |     86 |     93 |      0 |     94 |  68.25 |

# Notes:

#     Column titles are all centered
#     The printed output is sorted in ascending order based on the student IDs
#     Each column is seperated from a neighboring column(s) by three characters ' | ' 
#     (space vertical_bar space).
#     IDs are always 10 characters and they are left justified (not counting the 
#     boundary characters)
#     Names are left justified (maximum of 16 characters, not counting the boundary 
#     characters).
#     Grades and averages are right justified. The width of the columns for the grades 
#     and averages is 6 characters (not counting the boundary characters).
#     Averages are right justified with two digits of accuracy after the decimal point.

# Hint: Use the function which you developed in part 1 to read the input file and 
# create a dictionary. Use .format() to format the output. 

################### My function ###################
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
                    list_test.append(int(line[grade_1_index]))
                    flag_1 = 1
                elif ('Test_1' not in line) and (flag_1 == 0):
                    list_test.append(int(0))
                    flag_1 = 1
                elif ('Test_2' in line) and (flag_2 == 0):
                    grade_2_index = line.index('Test_2') + 1
                    list_test.append(int(line[grade_2_index]))
                    flag_2 = 1
                elif ('Test_2' not in line) and (flag_2 == 0):
                    list_test.append(int(0))
                    flag_2 = 1
                elif ('Test_3' in line) and (flag_3 == 0):
                    grade_3_index = line.index('Test_3') + 1
                    list_test.append(int(line[grade_3_index]))
                    flag_3 = 1
                elif ('Test_3' not in line) and (flag_3 == 0):
                    list_test.append(int(0))
                    flag_3 = 1
                elif ('Test_4' in line) and (flag_4 == 0):
                    grade_4_index = line.index('Test_4') + 1
                    list_test.append(int(line[grade_4_index]))
                    flag_4 = 1
                elif ('Test_4' not in line) and (flag_4 == 0):
                    list_test.append(int(0)) 
                    flag_4 = 1
        AVGERAGE = sum(list_test[1:]) / 4
        list_test.append(AVGERAGE)
    return out_dict

def print_grades(file_name):
    # Call your create_grades_dict() function to create the dictionary
    grades_dict = create_grades_dict(file_name)
    print('    ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |')
    key_sorted = sorted(grades_dict)
    for item in key_sorted:
        list_test = grades_dict[item]
        name, Test_1, Test_2, Test_3, Test_4, Avg = list_test
        string = "{0:<10d} | {1:<16} | {2:>6d} | {3:>6d} | {4:>6d} | {5:>6d} | {6:6.2f} |".format(int(item), name, Test_1, Test_2, Test_3, Test_4, Avg)
        print(string)

################### Driver Code Tester ###################
file_directory = '.\\17 - Assignment 4\\student_grades.txt'
print_grades(file_directory)

################### Instructor function ###################
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
    
def _print_grades(file_name):
    grade_dict=_create_grades_dict(file_name)
    ids=list(grade_dict.keys())
    ids.sort()
    print("{0:^10s} | {1:^16s} | {2:^6s} | {3:^6s} | {4:^6s} | {5:^6s} | {6:^6s} |".format('ID','Name','Test_1','Test_2','Test_3','Test_4','Avg.'))
    for id in ids:
        name=grade_dict[id][0]
        grades=grade_dict[id][1:5]
        average=grade_dict[id][5]
        print("{0:s} | {1:16s}".format(id,name),end="") 
        for grade in grades: # Print test scores
            print (" | {0:>6d}".format(grade),end="")
        print(" | {0:>6.2f} |".format(average))