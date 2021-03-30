str = "Hello 12345 World"
l =[]
for i in str:
    if i.isdigit():
        l.append(i)
    else:
        continue
print(l)