num = int(input("enter number to check "))
arm = str(num)
sum = 0
for i in arm:
    sum = sum + (int(i)**3)
if num == sum:
    print("number is an armstrong number")
else:
    print("number is not an armstrong number")

