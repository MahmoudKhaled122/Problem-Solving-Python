# write a python prgoram to get name , age from the user to check wether it is able to take participate in voting , or not if age is grater , or equal than 18 years you can take participate in the voting =>
# user_name = input("please enter the name of the user is : ")
# user_age = float(input("please enter the age of the user is = "))
# print("the name of the user is : \'"+user_name+"\'")
# print("the age of the user is = \'"+str(user_age)+" years\'")
# if((user_age >= 18)) :
#     print("HI \'"+user_name+"\' , you can take participation in the votting in the college , because the age of the user is = "+str(user_age)+" years")
# else :
#     print("SORRY \'"+user_name+"\' , you can not take participation in the votting in the college , because the age of the user is = "+str(user_age)+" years , and you need "+str(18 - user_age)+" years to take participation in the college")

# def check_user_college_votting(age , name) :
#     if(age >= 18) :
        # return("HI \'"+name+"\' , you can take participation in the votting in the college , because the age of the user is = "+str(age)+" years")
#     else :
#         return("SORRY \'"+name+"\' , you can not take participation in the votting in the college , because the age of the user is = "+str(age)+" years , and you need "+str(18 - age)+" years to take participation in the votting in the college")
# user_age = float(input("please enter the age of the user is = "))
# user_name = input("please enter the name of the user is : ")
# print("the name of the user is : \'"+user_name+"\'")
# print("the age of the user is = \'"+str(user_age)+" years\'")
# votting_in_college = check_user_college_votting(user_age , user_name)
# print(votting_in_college)

user_name = input("please enter the name of the user is : ")    
user_age = float(input("please enter the age of the user is = "))
def check_user_college_votting(name , age) :
    print("the name of the user is : \'"+name+"\'")
    print("the age of the user is = \'"+str(age)+" years\'")
    if(age >= 18) :
        print("HI "+name+" , you can take participation in the votting in the college , because your entered user age is = "+str(age)+" years")
    else :
        print("SORRY "+name+" , you can not take participation in the votting in the college , because your entered user age is = "+str(age)+" years , and you need "+str(18 - age)+" years to take participation in the votting in the college")
check_user_college_votting(user_name , user_age)
















# user_name = input("please enter the name of the user is : ")
# age = float(input("please enter the age of the user is : "))
# print("the name of the user is : \""+str(user_name)+"\"")
# print("the age of the user is : \""+str(age)+" years\"")
# if(age >= 18) :
#     print("HI \""+user_name+"!\" , you can be able to take participation in the votting , because your age is grater than , or equal to 18 years , and your entered age is : \""+str(age)+" years\"")
# else :
#     print("SORRY \""+user_name+"!\" , you can not take participation in the votting , because your entered age is less than 18 , your entered age is = \""+str(age)+" years\" , and you need : \""+str(18 - age)+" years\" to be able to take participation in the votting")
    