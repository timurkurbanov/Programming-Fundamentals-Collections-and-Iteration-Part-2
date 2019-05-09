#9.1
grocery_list = ["carrots", "toilet paper", "apples", "salmon"]
for item in grocery_list:
    print(f"* {item}")
#9.1
grocery_list.append('rise')
print(grocery_list)
#9.2
print(len(grocery_list))
#9.3
if 'bananas' in grocery_list:
    print("You need to pick up bananas")
else:
    print("You don't need to pick up bananas today")
#9.4
print (grocery_list[1])
#9.5
grocery_list.sort()
for item in grocery_list:
    print(f"* {item}")
#9.6
grocery_list.remove("salmon")
print(grocery_list)
#10

