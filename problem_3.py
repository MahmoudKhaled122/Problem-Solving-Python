# write a python program to calculate the area of the circle =>
import math 
# radius_of_circle = float(input("please enter the radius of the circle is = "))
# print("the radius of the circle is = "+str(radius_of_circle))
# # area_of_circle = math.pi * radius_of_circle * radius_of_circle 
# # area_of_circle = math.pi * radius_of_circle ** 2
# area_of_circle = math.pi * pow(radius_of_circle , 2)
# print("the area of the circle is = "+str(area_of_circle)+" , because your entered radius of the circle is = "+str(radius_of_circle))

# def get_area_of_circle(radius_of_circle) :
#     if(radius_of_circle > 0) :
# #         return("the area of the circle is = "+str(math.pi * radius_of_circle * radius_of_circle)+" , because your entered radius of the circle is = "+str(radius_of_circle))
#         #   return("the area of the circle is = "+str(math.pi * radius_of_circle ** 2 )+" , because your entered radius of the circle is = "+str(radius_of_circle))
#         return("the area of the circle is = "+str(math.pi  * pow(radius_of_circle , 2))+" , because your entered radius of the circle is = "+str(radius_of_circle))
#     elif(radius_of_circle == 0) :
# #         return("the area of the circle is = "+str(math.pi * radius_of_circle * radius_of_circle)+" , because your entered radius of the circle is = "+str(radius_of_circle))
#         #   return("the area of the circle is = "+str(math.pi  * radius_of_circle ** 2)+" , because your entered radius of the circle is = "+str(radius_of_circle))
#         return("the area of the circle is = "+str(math.pi  * pow(radius_of_circle , 2))+" , because your entered radius of the circle is = "+str(radius_of_circle))
#     else :
#         return("there is no area of the circle , because your entered radius of the circle is = "+str(radius_of_circle))
# radius_of_circle = float(input("please enter the radius of the angle is = "))
# print("the radius of the circle is = "+str(radius_of_circle))
# area_of_circle = get_area_of_circle(radius_of_circle)
# print(area_of_circle)

radius_of_circle = float(input("please enter the radius of the circle is = "))
def get_area_of_circle(rad_of_circle) :
    print("the area of the circle is = "+str(rad_of_circle))
    if(rad_of_circle > 0) :
        print("the area of the circle is = "+str(rad_of_circle ** 2 * math.pi)+" , because your entered radius of the circle is = "+str(radius_of_circle))
    elif(rad_of_circle == 0) :
        print("the area of the circle is = "+str(rad_of_circle ** 2 * math.pi)+" , because your entered radius of the circle is = "+str(radius_of_circle))
    else :
        print("there is no area of the circle , because your entered radius of the circle is = "+str(radius_of_circle))
get_area_of_circle(radius_of_circle)