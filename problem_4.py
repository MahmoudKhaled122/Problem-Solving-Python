# write a python program to get the area of the rectangle =>
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# print("the width of the rectangle is = "+str(width_of_rectangle))
# print("the length of the rectangle is = "+str(length_of_rectangle))
# area_of_rectangle = width_of_rectangle * length_of_rectangle 
# print("the area of the rectangle is = "+str(area_of_rectangle))

# def get_area_of_rectangle(wid_of_rectan , len_of_rectan) :
#     if((wid_of_rectan > 0) and (len_of_rectan > 0)) :
#         return ("the area of the rectangle is = "+str(wid_of_rectan * len_of_rectan))
#     elif((wid_of_rectan == 0) or (len_of_rectan == 0)) :
#         return("the area of the rectangle is = "+str(wid_of_rectan * len_of_rectan))
#     else :
#         return("there is no area of this rectangle , because the value of the length of the rectangle , or width of the rectangle is a negative value")
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# area_of_rectangle = get_area_of_rectangle(width_of_rectangle , length_of_rectangle)
# print("the width of the rectangle is = "+str(width_of_rectangle))
# print("the length of the rectangle is = "+str(length_of_rectangle))
# print(area_of_rectangle)

width_of_rectangle = float(input("please enter the width of the rectangle is = "))
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
def get_area_of_rectangle(wid_of_rectan , len_of_rectan) :
    print("the width of the rectangle is = "+str(wid_of_rectan))
    print("the length of the rectangle is = "+str(len_of_rectan))
    area_of_rectangle = len_of_rectan * wid_of_rectan
    if((len_of_rectan >= 0) and (wid_of_rectan >= 0)) :
        print("the area of the rectangle is = "+str(area_of_rectangle))
    else :
        print("there is no area of this rectangle , because the value of the length of the rectangle , or width of the rectangle is a negative values")
get_area_of_rectangle(width_of_rectangle , length_of_rectangle)