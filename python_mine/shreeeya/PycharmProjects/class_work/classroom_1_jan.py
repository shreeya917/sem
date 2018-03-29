my_str="abc"
my_list=[]
for letter in my_str:
    for index in range(len(my_str)):
        my_list.append((letter,index))
        print(my_list)

#Comprehension
my_list = [(letter, index) for letter in my_str for index in range(len(my_str))]
print(my_list)




nums = [5, 10, 15, 20, 25]
my_lis = []
for val in enumerate(nums):
    my_lis.append(val)
    print(my_lis)

#Comprehension
my_lis = [val for val in enumerate(nums)]

print(my_lis)




lang = ["Python", "Java", "C"]
creator = ["Guido Van Rossum", "James Gosling", "Denis Ritchi"]

my_dictionary = {}
for key, val in zip(lang,creator):
    my_dictionary[key]=val
    print(my_dictionary)

#Comprehension
my_dictionary={}
my_dictionary = {key:val for key, val in zip(lang, creator)}
print(my_dictionary)

lang = ["Python", "Java", "C", "linux"]
creator = ["Guido Van Rossum", "James Gosling", "Denis Ritchi", "Linus Torvalds"]

my_dictionary = {}
for key, val in zip(keys, values):
    if key != "linux":
        my_dictionary[key]=val
print(my_dictionary)

lang = ["Python", "Java", "C", "linux"]
creator = ["Guido Van Rossum", "James Gosling", "Denis Ritchi", "Linus Torvalds"]

my_dict = {key:val for key, val in zip(lang, creator)}
print(my_dict)


my_dictionary = {key:val for key, val in zip(lang, creator) if key != "linux"}
print(my_dictionary)

nums=[1,2,3,4,5]
my_set={val*val for val in nums}
print(my_set)

nu=(1,2,3,4,5)
print(type(nu))
my_s_tup=(n*n for n in nu)
print(my_s_tup)


# write a program that counts and print the numbers od each character in a string input by user
#example for following input:abaaabbba
#the output should be {'a':5, 'b':4}


