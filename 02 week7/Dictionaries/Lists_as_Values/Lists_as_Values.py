# a function that accepts a dictionary as input which contains
# the names and grades of students (The keys are student names
# and the values are lists of grades for 3 exams (1 Dimensional list))
# and returns the list of names for those students whose grade on all
# three exams is greater than or equal to 78.
def Lists_as_Values(your_dict):
    values = your_dict.values()
    values = list(values)
    my_list = []
    keys = your_dict.keys()
    keys = list(keys)
    for dim2 in values:
        count = 0
        for index in range(len(dim2)):
            if dim2[index] >= 78:
                count = count + 1
        if count == 3:
            my_list.append(keys[values.index(dim2)])
    return my_list

# driver code tester
my_dict = {'moha':[32, 54 , 102], 'amir':[78, 88, 91], 'morteza':[78, 78, 78]}
result = Lists_as_Values(my_dict)
print(result)