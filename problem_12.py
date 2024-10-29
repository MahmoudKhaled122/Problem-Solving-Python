# write a python program to get the union of the three sets =>
# frist_set = {5 , 12 , 52 , 0 , 8}
# second_set = {2 , 5 , 1 , 9 , 8}
# third_set = {4 , 5 , 6 , 0 , 10}
# print("the frist set is : "+str(frist_set))
# print("the second set is : "+str(second_set))
# print("the third set is : "+str(third_set))
# union_set = frist_set . union(second_set , third_set)
# print("the union of the three sets is : "+str(union_set))

frist_set = {5 , 12 , 52 , 0 , 8}
second_set = {2 , 5 , 1 , 9 , 8}
third_set = {4 , 5 , 6 , 0 , 10}
def union_of_three_sets(fri_set , sec_set , thi_set) :
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    print("the third set is : "+str(thi_set))
    union_set = fri_set . union(sec_set , thi_set)
    print("the union of the three sets is : "+str(union_set))
union_of_three_sets(frist_set , second_set , third_set)