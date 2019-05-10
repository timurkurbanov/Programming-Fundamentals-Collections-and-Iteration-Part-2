# #9.1
# grocery_list = ["carrots", "toilet paper", "apples", "salmon"]
# for item in grocery_list:
#     print(f"* {item}")
# #9.1
# grocery_list.append('rise')
# print(grocery_list)
# #9.2
# print(len(grocery_list))
# #9.3
# if 'bananas' in grocery_list:
#     print("You need to pick up bananas")
# else:
#     print("You don't need to pick up bananas today")
# #9.4
# print (grocery_list[1])
# #9.5
# grocery_list.sort()
# for item in grocery_list:
#     print(f"* {item}")
# #9.6
# grocery_list.remove("salmon")
# print(grocery_list)
#10.1
students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}
#10.2
# for key, value in students.items():
#         print("{}: {} students".format(key, value))  

#10.3
# students.update( {'cohort4': 43} )
# print(students)
#10.4

# keys = students.keys()

# print(keys)
#10.5
# for key, val in students.items():
#     students[key] *= 1.05
# print(students)
#10.6
#students.pop('cohort2')
#print(students)
#10.7

total = 0
for key, value in students.items():
  total = total + value
print(total)
