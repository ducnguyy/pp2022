
class Student:

    students = {}

    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob=dob

    @staticmethod
    def create():
        id=input("student id:")
        name=input("student name:")
        dob=input("student dob:")
        if id in Student.students:
            print("Id existed")
            return None 
        else:
            s=Student(id,name,dob)
            Student.students[s.id]=s
            return s
        
    @staticmethod
    def show():
        for student_id in Student.students:
            print(Student.students[student_id])

class Course:

    courses = {}

    def __init__(self, name, id):
        self.name = name
        self.id = id

    @staticmethod
    def create():
        id=input("course id:")
        name=input("course name:")
        if id in Course.courses:
            print("Id existed")
            return None
        else:
            course = Course(name, id)
            Course.courses[course.id] = course
            return course

class Mark(Course):
    
    marks = {}
    
    def __init__(self, course, student, id):
        super().__init__(course.name, course.id)
        self.student = student
        self.id = id
    
    @staticmethod
    def create():
        student_id=input("student id:")
        course_id=input("course id:")
        score = input("Grade:")
        Mark.marks[(student_id, course_id)] = score

    @staticmethod
    def lookup():
        student_id=input("student id:")
        course_id=input("course id:")
        print(Mark.marks[(student_id, course_id)])

Student.create()
Student.show()

math = Course.create()

Mark.create()
Mark.lookup()
print(math)

students = {}
courses = {}
marks = {}


id = "1"
students[id]
