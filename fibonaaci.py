num1 = 0
num2 = 1
ranges = 10
li = []
for i in range(ranges):
    num3 = num1+num2
    li.append(num3)
    num1, num2 = num2, num3
print(li)