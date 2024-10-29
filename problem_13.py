# write a python program to get the intersection of the two sets =>
# frist_set = {5 , 2 , 4 , 6 , 7 , 1}
# second_set = {5 , 3 , 12}
# print("the frist set is : "+str(frist_set))
# print("the second set is : "+str(second_set))
# intersection_set = frist_set . intersection(second_set)
# print("the intersection of the two sets is : "+str(intersection_set))

frist_set = {5 , 2 , 4 , 6 , 7 , 1}
second_set = {5 , 3 , 12}
def intersection_of_two_sets(fri_set , sec_set) :
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    intersection_set = frist_set . intersection(sec_set)
    print("the intersection of the two sets is : "+str(intersection_set))
intersection_of_two_sets(frist_set , second_set)