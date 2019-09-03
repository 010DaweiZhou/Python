
class MyClazz:
    clazz = 0

    def __init__(self, value):
        self.clazz = value

    def function(self):
        print('hello world!')

    def prt(self):
        print(self)
        print(self.__class__)


class People:
    name = ''
    age = 0
    weight = 0

    def __init__(self, name, age , weight):
        self.name = name
        self.age = age
        self.weight = weight

    def prt(self):
        print(self.name, ' ', self.age , ' ' ,self.weight)
        
x = MyClazz(100)
print(x.clazz)
x.function()
x.prt()

people = People('zhou', 20 , 66)
people.prt()


class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        People.__init__(self, name, age, weight)
        self.grade = grade
    
    def prt(self):
        print(self.name, ' ', self.age, ' ', self.weight , ' ' , self.grade)
        
student = Student('zhou', 20, 66, 'No.1')
student.prt()


class Speaker():
    topic = ''
    name = ''

    def __init__(self, topic, name):
        self.topic = topic
        self.name = name
    
    def prt(self):
        print('i\'m {name} , i speak {topic}'.format(name = self.name , topic = self.topic))
        
class Simple(Speaker, Student):
    
    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, topic, name)
    

simple = Simple('zhou', 20, 66, 'No.1', 'python')
simple.prt()


class father():

    def myMethod(self):
        print('here is father!')

class child(father):
    def myMethod(self):
        print('here is child!')


c = child()
c.myMethod()

class Justcounter:
    __selfCounter = 0
    publicCounter = 0

    def __selfAdd(self):
        self.__selfCounter += 1
        self.publicCounter += 1

    def count(self):
        self.__selfAdd()
        print(self.publicCounter, ' ', self.__selfCounter)
    

test = Justcounter()
test.count()
print(test.publicCounter)

class Vector:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return 'Vector(%d , %d)' % (self.a, self.b)
        
    def __add__(self, other):
        return Vector(self.a + other.a , self.b + other.b)

v1 = Vector(1,2)
v2 = Vector(3, 4)

print(v1 + v2)

