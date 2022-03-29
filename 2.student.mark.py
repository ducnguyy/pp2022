from pickle import TRUE
import copy

class students:
    def numstu(stu):
        stu.number1=int(input("student number:"))
        return stu.number1
    def stuinfo(stu):
        stu.name1=input("student name:")
        stu.id1=input("student id:")
        stu.dob1=input("student dob:")
        stu.prof1=(stu.id1,stu.dob1,stu.name1)
        return stu.name1, stu.id1, stu.dob1,stu.prof1
    def liststu(stu):
        stulist=[]
        for i in stu.number1:
            stulist.append(stu.prof1)   
    def showstu(stu):
        for i in stu.number1:
            print("student id: "stu.prof1[0]+" and student dob: "+stu.prof1[1]+" and student name: "+stu.prof1[3])
class courses:
    def numcour(course):
        course.number2=int(input("course number:"))
        return course.number2
    def courinfo(course):
        course.name2=input("course name:")
        course.id2=input("course id:")
        return course.name2, course.id2

student=students()
student.numstu()
student.showstu()





