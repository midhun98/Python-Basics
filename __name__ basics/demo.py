from Calc import add

print("__name__ is ", __name__)


def fun1():
	add()
	print("from fun1")


def fun2():
	print("from fun2")


def main():
	fun1()
	fun2()


main()
