def isArmstrong(number):
    total = 0
    for n in str(number):
        total += int(n) ** 3
    return number == total


x = 153
print(isArmstrong(x))
