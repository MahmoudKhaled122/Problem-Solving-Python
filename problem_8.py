# write a python program to get name , and total marks from the user to check wether be able to take admission in the college , or not , if total marks grater than , or equal to 60 , you will take admission in the college =>
# user_name = input("please enter the name of the user is : ")
# user_total_marks = float(input("please enter the total marks of the user is = "))
# print("the name of the user is : \'"+user_name+"\'")
# print("the total marks of the user is : \'"+str(user_total_marks)+" marks\'")
# if(user_total_marks >= 60) :
#     print("HI \'"+user_name+"\' , you can take admmission in the college , because the total marks of the user is = "+str(user_total_marks)+" marks")
# else :
#     print("SORRY \'"+user_name+"\' , you can not take admmission in the college , because the total marks of the user is = "+str(user_total_marks)+" marks , and you need "+str(60 - user_total_marks)+" marks to take admmission in the college")

# user_name = input("please enter the name of the user is : ")
# user_total_marks = float(input("please enter the total marks of the user is = "))
# def check_user_total_marks(name , total_marks) :
#     print("the name of the user is : \'"+name+"\'")
#     print("the total marks of the user is = \'"+str(total_marks)+" marks\'")
#     if(total_marks >= 60) :
#         print("HI \'"+name+"\' , you can take addmission in the college , because your total marks of the user is = "+str(total_marks)+" marks")
#     else :
#         print("SORRY \'"+name+"\' , you can not take addmission in the college , because your total marks of the user is = "+str(total_marks)+" marks , and you need "+str(60 - total_marks)+" marks to take addmission in the college")
# check_user_total_marks(user_name , user_total_marks)

def check_user_total_marks(name , total_marks) :
    if(total_marks >= 60) :
        return("HI \'"+name+"\' , you can take addmission in the college , because your total marks of the student is = "+str(total_marks)+" marks")
    else :
        return("SORRY \'"+name+"\' , you can not take addmission in the college , because your total marks of the student is = "+str(total_marks)+" marks , and you need "+str(60 - total_marks)+" marks to take addmission in the college")
user_name = input("please enter the name of the user is : ")
user_total_marks = float(input("please enter the total marks of the user is = "))
print("the name of the user is : \'"+user_name+"\'")
print("the total marks of the user is = "+str(user_total_marks)+" marks")
check_user_take_addmission_in_college = check_user_total_marks(user_name , user_total_marks)
print(check_user_take_addmission_in_college)