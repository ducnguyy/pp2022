from pickle import TRUE
import copy

def inputfunct():
    number_of_students=int(input("Input number of your student in this class:"))
    student_dictionary={}
    for orderstu in range(1,number_of_students+1):
        check=1
        while check==True:
            student_ID=input("Input ID of student number "+str(orderstu)+":")
            if student_ID not in student_dictionary:
                check=0
            else:
                print("There's already exist a student with this ID!")
        student_name=input("Input name of student number "+str(orderstu)+":")
        student_dob=input("Input DoB of student number "+str(orderstu)+":")
        totalinfo=[]
        totalinfo.append(student_name)
        totalinfo.append(student_dob)
        student_dictionary[student_ID]=totalinfo
    numcourse=int(input("Input number of courses:"))
    if numcourse==0:
        return print("There's no course.")
    course_dict={}
    for ordercourse in range(1,numcourse+1):
        courseID=input("Input course number "+str(ordercourse)+" ID:")
        courseID=courseID.lower()
        courseID=courseID.replace(" ","")
        coursename=input("Input course number "+str(ordercourse)+" name:")
        courselist=[]
        courselist.append(coursename)
        course_dict[courseID]=courselist
    b=1
    for i in (course_dict):
        print("Course number "+str(b)+": ID: "+i+"; Name: "+str(course_dict[i]))
        b+=1
    chosen=input("Select 1 course by input its ID: ")
    chosen=chosen.lower()
    chosen=chosen.replace(" ","")
    print("this is marksheet of "+course_dict[chosen][0]+": ")
    for orderstu in student_dictionary:
       student=[]
       student.append(orderstu)
       mark=int(input("Write mark of "+student_dictionary[orderstu][0]+": "))
       student.append(mark)
       (course_dict[chosen]).append(student)
    print("Done inputting mark of students.")
    return student_dictionary, course_dict
    
def outputfunct(init_stu_dict,init_cour_dict):
    for i in init_cour_dict:
        print("Courses ID: "+i+", Name: "+init_cour_dict[i][0])
    for i in init_stu_dict:
        print("Student ID: "+i+", name: "+init_stu_dict[i][0]+", DoB: "+init_stu_dict[i][1])
    chosen=input("Choose a course by its ID: ")
    chosen=chosen.lower()
    chosen=chosen.replace(" ","") 
    print("You chose course: "+init_cour_dict[chosen][0])

    f=0
    for item in init_cour_dict[chosen]:
        f+=1
    print(f)
    for i in range(1,f):
        print("Student ID: "+init_cour_dict[chosen][i][0]+", Name: "+init_stu_dict[init_cour_dict[chosen][i][0]][0]+" , mark: "+str(init_cour_dict[chosen][i][1]))
    return 0
init_stu_dictglo, init_cour_dictglo= inputfunct()
outputfunct(init_stu_dictglo,init_cour_dictglo)



