
students = []

print("=" * 60)
print("              STUDENT MANAGEMENT SYSTEM")
print("=" * 60)
print("              Developed & Founded By")
print("              MD. MOJAHIDUR RAHMAN SAJID")
print("              Computer Science & Technology")
print("              Bogura Polytechnic Institute")
print("=" * 60)
def add_student():
    name=input('enter student name:  ')
    roll=int(input('enter roll:   '))
    department=input('enter department:  ')

    bangla = int(input('enter bangla mark :  '))
    english = int(input('enter english mark :   '))
    python = int(input('enter python mark :'))
    dsa = int(input('enter DSA mark :  '))

    student={
        'name':name,
        'roll':roll,
        'department':department,
        'mark':[bangla,english,python,dsa]
    }
    students.append(student)
    
def show_student():
    for student in students:
        print('-----------------------------------')
        print(f'name : {student["name"]}')
        print(f'roll: {student["roll"]}')
        print(f'department: {student["department"]}')
        print(f'mark:{student["mark"]}')
def search_student():
    roll=int(input('enter roll : '))
    found = False
    for student in students:
        if student['roll']==roll:
            print(student)
            found=True
            break
    if not found:
        print('student not found ')

def delete_student():
    roll=int(input('enter roll : '))
    found = False
    for student in students:
        if student['roll']==roll:
            students.remove(student)
            print('student deleted succssfully')
            found=True
            break
    if not found:
        print('student not found ')

def avareg_mark():
    roll=int(input('enter roll: '))
    found = False

    for student in students:
        if student['roll']==roll:
            print(f'student found : {student["name"]}')
            total=sum(student['mark'])
            avareg=total/len(student['mark'])
            print(f'average mark = {avareg}')
            found=True
            break 
    if not found:
        print('student not found ')
def update_student():
    roll=int(input('enter roll : '))
    found=False
    for student in students:
        if student['roll']==roll:
            print(f'student found : {student["name"]}')
            
            new_name=input('enter new name :    ')
            student['name']=new_name
            new_marks = list(map(int, input("Enter new marks: ").split()))
            student["mark"] = new_marks
            print('student updated successfully  ')
            found=True
            break
    if not found:
        print('sorry student is not found ')
while True:
    print()
    print('='*20)
    print('        MAIN MENU ')
    print('='*20)
    print('1. Add student ')
    print('2. Show student ')
    print('3. Search student ')
    print('4. Delete student ')
    print('5. Average mark ')
    print('6. Update student ')
    print('7. Exit ')
    choice=input('enter your choice : ')
    if choice=='1':
        add_student()
    elif choice=='2':
        show_student()
    elif choice=='3':
        search_student()
    elif choice=='4':
        delete_student()
    elif choice=='5':
        avareg_mark()
    elif choice=='6':
        update_student()
    elif choice=='7':
        print('Thank you for using student management system .')
        break
    else:
        print("Invalid choice. Please try again.")