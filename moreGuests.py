list = ['A', 'B', 'C']
print("we found more room on dinner table")
list.insert(0,'D')
list.insert(len(list)//2,'E')
list.append('F')
for i in list:
    print(i,"you are invited to dinner")