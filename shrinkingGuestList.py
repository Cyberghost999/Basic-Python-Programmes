list = ['A', 'B', 'C', 'D', 'E', 'F']
print("Sorry, we have room for only 2 people")
for i in range(0, 4):
    print("Sorry", list[1], "you are not invited to dinner")
    list.pop(1)
for x in list:
    print(x, "you are still invited")