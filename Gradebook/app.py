from Student import Student

students = []

def prompt():
  task = input('Do you want to:\n(1) Create new student\n(2) Change a students grade\n(3) View Students\n')
  if task == '1':
    newStudent = input('What is the students name:\n')
    if len(students) >= 1:
      for student in students:
        if newStudent == student.name:
          print('Student already created')
        else:
          print('student added')
          addStudent(newStudent)
    else:
      addStudent(newStudent)
  elif task == '2':
    selectedStudent = input('What is the students name:\n')
    newGrade = input('What is the new grade\n')
    for student in students:
      if student.name.lower() == selectedStudent.lower():
        student.setGrade(newGrade)
      else:
        print('No Such Student')
  elif task == '3':
    print('Name | Grade \n')
    for student in students:
      print(student.name + ' | ' + str(student.grade))
  prompt()


def addStudent(name):
  students.append(Student(name))



prompt()