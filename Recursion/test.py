def printNum(num):
    print(num)
    num -= 1
    if num == 0:
        return

    printNum(num)


printNum(5)
