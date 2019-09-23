
import time


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def prei(self):
        return (self.length + self.width) * 2


rr = Rectangle(10, 20)
print(rr.area())
print(rr.prei())


class CapStr(str):

    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


cc = CapStr('hello world!')
print(cc)


class C:

    def __init__(self):
        print('i\'m init ...')

    def __del__(self):
        print('i\'m del ...')


c1 = C()
c2 = c1
c3 = c2

del c1
del c2
del c3


class MyInt(int):

    def __add__(self, other):
        return int(self) + int(other)

    def __sub__(self, other):
        return int(self) - int(other)


m1 = MyInt(1)
m2 = MyInt(2)

print(m1 + m2)


class Nint(int):
    # just a test
    def __radd__(self, other):
        return int(self) - int(other)


n1 = Nint(10)
n2 = Nint(20)

print(n1 + n2)
print(1 + n2)


class MyTimer():

    def __init__(self):
        self.t_start = 0
        self.t_stop = 0
        self.interval = 0

    def start(self):
        self.t_start = time.time_ns()

    def stop(self):
        self.t_stop = time.time_ns()
        result = self.__caculate()
        print('over ... time %ss' % str(result))

    def __caculate(self):
        self.interval = self.t_stop - self.t_start
        return self.interval

    def __str__(self):
        return str(self.interval) + 'ns'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self.interval + other.interval


mm = MyTimer()
mm.start()
time.sleep(0.001)
mm.stop()

print(mm)

