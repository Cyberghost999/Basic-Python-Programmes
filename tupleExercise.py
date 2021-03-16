menu = ('A', 'B', 'C')
for i in menu:
    print(i)
# menu[1] = 'D'
newMenu = list(menu)
newMenu[0] = 'D'
newMenu[1] = 'E'
menu = tuple(newMenu)
print("New list is ")
for x in menu:
    print(x)