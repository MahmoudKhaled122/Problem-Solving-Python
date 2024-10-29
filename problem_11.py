# write a python program to get the union of the two sets =>
# frist_set = {3 , 2 , 4 , 5 , 6 , 7 , 8}
# second_set = {4 , 12 , 5 , 1 , 6 , 8}
# print("the frist set is : "+str(frist_set))
# print("the second set is : "+str(second_set))
# union_set = frist_set . union(second_set)
# print("the union of the two sets is : "+str(union_set))

frist_set = {3 , 2 , 4 , 5 , 6 , 7 , 8 }
second_set = {4 , 12 , 5 , 1 , 6 , 8}
def union_of_two_sets(fri_set , sec_set) :
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    union_set = fri_set . union(sec_set)
    print("the union of the two sets is : "+str(union_set))
union_of_two_sets(frist_set , second_set)