# The class `Computer` has attributes for CPU and RAM, a method to configure the computer with a GPU,
# and an instance `com1` with specific CPU, RAM, and GPU configurations.

"""
__init__ basics
"""


class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self, gpu):
        print(gpu)
        print("Config is ",self.cpu, self.ram)

com1 = Computer('i5',16)
com1.config('RTX GPU')
