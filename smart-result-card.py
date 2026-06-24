print('------------------------- smart result card -------------------------')
print()
print()

while True:
    try:
        students = int(input('kitna students ka result card bnana hai : '))

        if students > 0:
            break
        else:
            print('students 1 ya us se zyada hone chahiye')

    except:
        print('sirf numbers allowed han alphabets nhi')


subjects = ('English', 'Maths', 'Physics', 'Chemistry', 'Computer')

student_names = []
student_percentages = []
student_totals = []

max_marks = len(subjects) * 100


for i in range(students):

    print()
    print(f'--------------- student {i+1} ka result ----------------------')

    name = input('student ka name batao : ')
    total_num = []

    for a in subjects:

        while True:
            try:
                num = int(input(f'apna {a} ka marks batao : '))

                if num >= 0 and num <= 100:
                    total_num.append(num)
                    print()
                    break
                else:
                    print('Marks 0 se 100 ke darmiyan hone chahiye')

            except:
                print('sirf numbers allowed han alphabets nhi')


    total_marks = sum(total_num)
    highest = max(total_num)
    lowest = min(total_num)
    percentage = (total_marks / max_marks) * 100

    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'


    if lowest < 33 or percentage < 50:
        status = 'fail'
        grade = 'F'
    else:
        status = 'pass'


    student_names.append(name)
    student_percentages.append(percentage)
    student_totals.append(total_marks)


    print('------------------- result card --------------------------------')
    print(f'student name : {name}')
    print(f'total marks : {total_marks}/{max_marks}')
    print(f'highest marks : {highest}')
    print(f'lowest marks : {lowest}')
    print(f'percentage : {percentage:.2f}%')
    print(f'grade : {grade}')
    print(f'status : {status}')
    print('-----------------------------------------------------------------')
    print()
    print()


print('-------------------- class summary -------------------------')

print(f'total students : {students}')

class_average = sum(student_percentages) / students
print(f'class average : {class_average:.2f}%')

topper_percentage = max(student_percentages)
topper_index = student_percentages.index(topper_percentage)

topper_name = student_names[topper_index]
topper_marks = student_totals[topper_index]

print(f'topper name : {topper_name}')
print(f'topper marks : {topper_marks}/{max_marks}')
print(f'topper percentage : {topper_percentage:.2f}%')

print('------------------------------------------------------------')
