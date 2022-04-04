from pickle import TRUE
import copy

class students:
    stuinfor={}
    def numstu(stu):
        stu.number1=int(input("student number:"))
        return stu.number1
    def stuinfo(stu):
        stu.infor1={}
        for i in range(0,stu.number1):
            stu.name1=input("student name:")
            stu.id1=input("student id:")
            stu.dob1=input("student dob:")
            stu.infor1[stu.id1]=(stu.dob1,stu.name1)
        return stu.infor1 
    def showstu(stu):
        for i in stu.infor1:
            print("student id: "+i+" and student dob: "+stu.infor1[i][0]+" and student name: "+stu.infor1[i][1])
class courses:
    def numcour(course):
        course.number2=int(input("course number:"))
        return course.number2
    def courinfo(course):
        course.dict={}
        for i in range(0,course.number2):
            course.name2=input("course name:")
            course.id2=input("course id:")
            course.dict[course.id2]=course.name2
        return course.dict
    def courdisplay(course):
        for i in course.dict:
            print("ID:"+i+"name:"+course.dict[i])
    def markinfo(course):
        course.markcheck=input("id of course need:")
        print("you accessing "+course.dict[course.markcheck])
        return course.markcheck
    def makeclass(course):
        course.subinfo=copy.deepcopy(course.dict)
        return course.subinfo
class mark(students,courses): 
    def markinput(class1):
        class1.studinfo=copy.deepcopy(class1.infor1)
        for i in class1.infor1:
            print("name:"+class1.infor1[i][1])
            x=int(input("mark of him/her:"))
            class1.studinfo[i]=x
        class1.subinfo[class1.markcheck]=class1.studinfo
        print(class1.subinfo)
    def markdisplay(class1):
        for j in class1.subinfo:
            print("name of course:"+class1.dict[j])
            for i in class1.infor1:
                print("name: "+class1.infor1[i][1])
                print("mark: "+str(class1.subinfo[int(j)][int(i)]))

            



class2=mark()
class2.numstu()
class2.stuinfo()
class2.numcour()
class2.courinfo()
class2.makeclass()
class2.markinfo()
class2.markinput()
class2.markdisplay()









