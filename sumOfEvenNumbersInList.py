list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum = 0
for i in list:
    if i%2 == 0:
        sum = sum+i
    else: 
        continue
print(sum)