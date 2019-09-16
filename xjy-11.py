
class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    number = 10

    def climb(self):
        print('climbing...')

tt = Turtle()
tt.climb()


class Ball():
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def kick(self):
        print('my name is %s' % self.name)

bb = Ball('kangkang')
bb.kick()
bb.setName('jane')
bb.kick()


class Person():

    __name = 'kangkang'
    # name = 'kangkang'

    def getName(self):
        return self.__name

pp = Person()
print(pp.getName())


print(pp._Person__name)

class Parent():
    def hello(self):
        print('hello , i\'m father')

class Child(Parent):
    pass

pp = Parent()
cc = Child()

pp.hello()
cc.hello()

import random as r
class Fish():

    number = 1

    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    
    def move(self):
        self.x -= 1
        print(self.x, ' ', self.y)

class Carp(Fish):
    pass

cc = Carp()
cc.move()

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True
    
    def eat(self):
        if self.hungry == True:
            print('i will eat')
            self.hungry = False
        else:
            print('i will not eat')
        
ss = Shark()
ss.eat()
ss.eat()
ss.move()


class Base1():
    def foo1(self):
        print('i\'m in base 1')

class Base2():
    def foo2(self):
        print('i\'m in base 2')

class C(Base1, Base2):
    pass

cc = C()
cc.foo1()
cc.foo2()

class Pool:
    def __init__(self,turtle,fish):
        self.turtle = turtle
        self.fish = fish
    
    def print_num(self):
        print('%d turtle and %d fish in pool' % (self.turtle.number, self.fish.number))

pp = Pool(Turtle(),Fish())
pp.print_num()

class C1:
    count = 0

    def x(self):
        print(5)

a = C1()
b = C1()
c = C1()

print(a.count, b.count, c.count)
c.count += 10
print(a.count, b.count, c.count)
C1.count += 100
print(a.count, b.count, c.count)

a.x = 10
print(a.x)
# a.x()

class XY():
    def printXY(self):
        print('no zuo no die')
    def setXY(self, x, y):
        self.x = x
        self.y = y

xy = XY()
xy.printXY()
print(xy.__dict__)
print(XY.__dict__)
xy.setXY(1, 2)
print(xy.__dict__)
print(XY.__dict__)

del XY
xy.printXY()

ff = Fish()
result = hasattr(ff, 'x')
print(result)
result = hasattr(ff, 'z')
print(result)
result = getattr(ff, 'z','no found!')
print(result)

setattr(ff, 'z', 10)
result = getattr(ff, 'z','no found!')
print(result)

delattr(ff, 'z')
result = getattr(ff, 'z','no found!')
print(result)







