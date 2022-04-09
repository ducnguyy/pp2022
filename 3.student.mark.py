import math
import numpy

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

    def __init__(self, name, id, weight):
        self.name = name
        self.id = id
        self.weight=weight

    @staticmethod
    def create():
        print("Creating course's profile:\n________________")
        id=input("Course's id: ")
        name=input("Course's name: ")
        weight=input("Course's credit points: ")
        if id in Course.courses:
            print("There's a course with this ID existed")
            return None
        else:
            course = Course(name, id, weight)
            Course.courses[course.id] = course
            return course
    @staticmethod
    def show():
        for course_id in Course.courses:
            print("Showing course's name and IDs: ")
            print(f"Name: {Course.courses[course_id].name}")
            print(f"ID: {Course.courses[course_id].id}")
            print(f"Credit points: {Course.courses[course_id].weight}")
    def find(course_id):
        if(course_id in Course.courses):
            return Course.courses[course_id]
        else:
            print("There's no course with this ID.")
            return None
    @staticmethod
    def Totalweight():
        total_weight=0
        for i in Course.courses:
            total_weight+=int(Course.courses[i].weight)
        return total_weight
        

class Mark(Course):
    
    marks = {}
    tuple=(Course.courses,Student.students)


    def __init__(self, course, student, score, weightscore):
        super().__init__(course.name, course.id,course.weight)
        self.student = student
        self.id = id
        self.score= score
        self.weightscore=weightscore
    
    @staticmethod
    def create():
        print("Type the corresponding ID for student and course.\n_________________")
        student_id=input("Student id: ")
        course_id=input("Course id: ")
        score = input("Add grade: ")
        score=math.floor(score)
        student1=Student.find(student_id)
        course1=Course.find(course_id)
        weightscore=(int(course1.weight))*int(score)
        newmark=Mark(course1,student1,score,weightscore)
        Mark.marks[(student_id, course_id)] = newmark
        
    def __repr__(self):
        return "Student ID " + str(self.student) + " in course ID " + str(self.id) + " has mark" + str(self.score) + ""
    @staticmethod
    def show():
        for (student_id,course_id) in Mark.marks:
            print(f"Student name: {Student.students[student_id].name} in course : {Course.courses[course_id].name} has mark: {Mark.marks[(student_id,course_id)].score}")
    @staticmethod
    def find(student_id,course_id):
        if (student_id,course_id) in Mark.marks:
            return Mark.marks[(student_id, course_id)]
        else:
            print("There's no student or course with input ID.")
            return None
    
    @staticmethod
    def WeightedSum():
        sumscore=0
        print(f"Search for GPA: ")
        student_id=input("Student ID:")
        for i in Mark.marks:
            if student_id in i:
                sumscore+=int(Mark.marks[i].weightscore)
        return sumscore/int(Course.Totalweight())

numberofstudentinput=input("Number of student in class: ")
numberofstudent=int(numberofstudentinput)
for i in range(1,(numberofstudent)+1):
    Student.create()
    Student.show()
numberofcourseinput=input("Number of course in class: ")
numberofcourse=int(numberofcourseinput)
for i in range(1,(numberofcourse)+1):
    Course.create()
a=1
while a:
    Mark.create()
    i=input("Continue writing? \n0=no,1=yes")
    a=int(i)
def markfind():
    print("finding grade:")
    student_id=input("student id:")
    course_id=input("course id:")
    mark1=Mark.find(student_id,course_id)
    print(mark1.score)
    print(mark1.weightscore)
markfind()
print(Mark.WeightedSum())
Student.show()
Course.show()
Mark.show()


