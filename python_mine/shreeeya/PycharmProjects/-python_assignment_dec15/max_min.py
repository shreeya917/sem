#Q2. Given a list of integers, my_list = [4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45].
# Find the maximum and minimum numbers in the list.

my_list = [4,2,4,0,2,4,5,7,8,9,23,8,5,4,2,2,34,4,45]
sorted_my_list=sorted(my_list)
print("The minimum number is:",my_list[0])
i=len(my_list)
print("The maximum number is:",my_list[i-1])