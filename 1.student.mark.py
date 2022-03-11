from pickle import TRUE

number_of_students=int(input("Input number of your student in this class:"))
student_dictionary={}
for orderstu in range(1,number_of_students+1):
    student_ID=input("Input student ID:")
    student_name=input("Input student name:")
    student_dob=input("Input student DoB:")
    totalinfo=[]
    totalinfo.append(student_name)
    totalinfo.append(student_dob)
    student_dictionary[student_ID]=totalinfo
    print(student_dictionary)
    

