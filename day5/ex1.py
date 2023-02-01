# Average student height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f'The total height is: {total_height}')

total_students = 0
for students in student_heights:
    total_students += 1
print(f'the number of students is: {total_students}')

average_height = total_height / total_students
print(f'the average height is: {round(average_height)}')
