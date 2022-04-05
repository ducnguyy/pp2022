
class Student:
    students = {}
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob=dob

    @staticmethod
    def create():
        print("Creating student's profile:\n__________________")
        name=input("Student name: ")
        id=input("Student ID: ")
        dob=input("Student dob: ")
        print("____________________")
        if id in Student.students:
            print("Student with this ID has already existed.")
            print("_____________________")
            return None 
        else:
            s=Student(name,id,dob)
            Student.students[s.id]=s
            return s
        
    @staticmethod
    def show():
        for student_id in Student.students:
            print("Showing students name and DOBs: ")
            print(f"Name: {Student.students[student_id].name}")
            print(f"DOB: {Student.students[student_id].dob}")
    @staticmethod
    def find(student_id):
        print(f"Finding student with ID:{student_id}")
        if(student_id in Student.students):
            print("There's a student with this ID.")
            print(Student.students[student_id])
            return Student.students[student_id]
        else:
            print("There's no student with this ID.")
            return None
class Course:

    courses = {}

    def __init__(self, name, id):
        self.name = name
        self.id = id

    @staticmethod
    def create():
        print("Creating course's profile:\n________________")
        id=input("Course id:")
        name=input("Course name:")
        if id in Course.courses:
            print("There's a course with this ID existed")
            return None
        else:
            course = Course(name, id)
            Course.courses[course.id] = course
            return course
    def find(course_id):
        if(course_id in Course.courses):
            return Course.courses[course_id]
        else:
            print("There's no course with this ID.")
            return None
        

class Mark(Course):
    
    marks = {}
    tuple=(Course.courses,Student.students)


    def __init__(self, course, student, score):
        super().__init__(course.name, course.id)
        self.student = student
        self.id = id
        self.score= score
    
    @staticmethod
    def create():
        print("Type the corresponding ID for student and course.\n_________________")
        student_id=input("Student id:")
        course_id=input("Course id:")
        score = input("Grade:")
        student1=Student.find(student_id)
        course1=Course.find(course_id)
        newmark=Mark(course1,student1,score)
        Mark.marks[(student_id, course_id)] = newmark
        


    @staticmethod
    def find(student_id,course_id):
        if (student_id,course_id) in Mark.marks:
            return Mark.marks[(student_id, course_id)]
        else:
            print("There's no student or course with input ID.")
            return None

numberofstudent=input(print("Number of student in class: "))
for i in range(0,int(numberofstudent)):
    Student.create()
    Student.show()
numberofcourse=input(print("Number of course in class: "))
for i in (0,int(numberofcourse)):
    Course.create()
a=1
while a:
    Mark.create()
    i=input("Continue writing? 0=no,1=yes")
    a=int(i)
def markfind():
    print("finding grade:")
    student_id=input("student id:")
    course_id=input("course id:")
    mark1=Mark.find(student_id,course_id)
    print(mark1.score)
    Student.find(student_id)
markfind()



