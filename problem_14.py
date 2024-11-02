# write a python program to get the intersection of three sets =>
# frist_set = {5 , 2 , 4 , 6 , 7 , 1}
# second_set = {4 , 5 , 12 , 1 , 2 , 0}
# third_set = {5 , 3 , 12}
# print("the frist set is : "+str(frist_set))
# print("the second set is : "+str(second_set))
# print("the third set is : "+str(third_set))
# intersection_set = frist_set . intersection(second_set , third_set)
# print("the intersection of the three sets is : "+str(intersection_set))

frist_set = {5 , 2 , 4 , 6 , 7 , 1}
second_set = {4 , 5 , 12 , 1 , 2 , 0}
third_set = {5 , 3 , 12}
def intersection_of_three_sets(fri_set , sec_set , thi_set) :
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    print("the third set is : "+str(thi_set))
    intersection_set = frist_set . intersection(second_set , third_set)
    print("the intersection of the three sets is : "+str(intersection_set))
intersection_of_three_sets(frist_set , second_set , third_set)