#Question 3b#
mark_ranges = ['90-100', '80-89', '70-79', '60-69', '0-59']
grades = ['A', 'B', 'C', 'D', 'F']

res = {}
for key in mark_ranges:
    for value in grades:
        res[key] = value
        grades.remove(value)
        break

print("The mark ranges and grades are: " + str(res))

print("The mark_ranges and grades are: " + str(res))

mark_ranges = ('90-100', '80-89', '70-79', '60-69', '0-59')
grades = ('A', 'B', 'C', 'D', 'F')
x = 0
while x<=4:
    print (grades[x], mark_ranges[x])
    x = x+1
