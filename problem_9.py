# write a python program to perform all arthimetic operations on two variables => 
# frist_num = float(input("please enter the frist number is = "))
# second_num = float(input("please enter the second number is = "))
# print("\n")
# print("the values of the two numbers is : \n")
# print("the value of the frist number is = "+str(frist_num))
# print("the value of the second number is = "+str(second_num))
# print("the result of the all arthimetic operations into two values of the two numbers is : \n")
# print("the result of the addition arthimetic operation of the two numbers is = "+str(frist_num + second_num))
# print("the result of the subtraction arthimetic operation of the two numbers is = "+str(frist_num - second_num))
# print("the result of the multiplication arthimetic operation of the two numbers is = "+str(frist_num * second_num))
# print("the result of the division arthimetic operation of the two numbers is = "+str(frist_num / second_num))
# print("the result of the modulus arthimetic operation of the two numbers is = "+str(frist_num % second_num))

frist_number = float(input("please enter the frist number is = "))
second_number = float(input("please enter the second number is = "))
def get_all_arthimetic_operations_in_two_numbers(frist_num , second_num) :
    print("\n")
    print("the values of the two numbers is : \n")
    print("the value of the frist number is = "+str(frist_num))
    print("the value of the second number is = "+str(second_num))
    print("the result of the arthimetic operations into two values of the two numbers is : \n")
    print("the result of the addition arthimetic operation of the two numbers is = "+str(frist_num + second_num))
    print("the result of the subtraction arthimetic operation of the two numbers is = "+str(frist_num - second_num))
    print("the result of the multplication arthimetic operation of the two numbers is = "+str(frist_num * second_num))
    print("the result of the division arthimetic operation of the two numbers is = "+str(frist_num / second_num))
    print("the result of the modulus arthimetic operation of the two numbers is = "+str(frist_num % second_num))
get_all_arthimetic_operations_in_two_numbers(frist_number , second_number)