
class Student:

    students = {}
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob=dob

    @staticmethod
    def create():
        name=input("student name:")
        id=input("student id:")
        dob=input("student dob:")
        if id in Student.students:
            print("Id existed")
            return None 
        else:
            s=Student(name,id,dob)
            Student.students[s.id]=s
            return s
        
    @staticmethod
    def show():
        for student_id in Student.students:
            print(Student.students[student_id].name)
            print(Student.students[student_id].dob)
    @staticmethod
    def find(student_id):
        if(student_id in Student.students):
            return Student.students[student_id]
        else:
            print("there's no student id")
            return None
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
    def find(course_id):
        if(course_id in Course.courses):
            return Course.courses[course_id]
        else:
            print("there's no course id")
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
        student_id=input("student id:")
        course_id=input("course id:")
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
            print("there's none")
            return None

Student.create()
Student.show()

math = Course.create()

Mark.create()
student_id=input("student id:")
course_id=input("course id:")
mark1=Mark.find(student_id,course_id)
print(mark1.score)
Student.find(student_id)


