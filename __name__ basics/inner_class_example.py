class Student:
	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()

	def show(self):
		print(self.name, self.rollno)
		self.lap.show()

	class Laptop:
		def __init__(self):
			self.brand = "Hp"
			self.cpu = "i5"
			self.ram = 8

		def show(self):
			print(self.brand, self.cpu, self.ram)


s1 = Student("Midhun", 2)

s1.show()

lap1 = Student.Laptop()

# lap1 = s1.lap
#
# print(id(lap1))
# print(id(lap2))
