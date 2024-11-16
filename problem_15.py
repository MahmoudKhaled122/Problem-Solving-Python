# write a python program to get the difference between two sets =>
# frist_set = {1 , 12 , 2 , 6 , 7 , 8}
# second_set = {15 , 0 , 1 , 3 , 6}
# print("the frist set is : "+str(frist_set))
# print("the second set is : "+str(second_set))
# difference_set = frist_set . difference(second_set)
# print("the difference between the frist set , and second set is : "+str(difference_set))
# difference_set = second_set . difference(frist_set)
# print("the difference between the second set , and frist set is : "+str(difference_set))

frist_set = {1 , 12 , 2 , 6 , 7 , 8}
second_set = {15 , 0 , 1 , 3 , 6}
def difference_between_two_sets(fri_set , sec_set) :
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    difference_set = fri_set . difference(sec_set)
    print("the difference between the frist set , and second set is : "+str(difference_set))
    difference_set = sec_set . difference(fri_set)
    print("the difference between the second set , and frist set is : "+str(difference_set))
difference_between_two_sets(frist_set , second_set)