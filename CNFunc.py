import math
import random


def printRandValue(a):
    print(a)
    return


printRandValue(random.randint(0, 100))


def hello():
    print("hello world!\n")


hello()


def area(length, width):
    return length * width


length = width = 100
print("length = ", length, "width = ", width, "area = ", area(length, width))


def welcome(name):
    print("welcome " + name)


welcome("zhou")


def changeA(a):
    a += 100


a = 100
changeA(a)
print(a)


def changeList(myList):
    myList.append(1)
    print(myList)
    return


list = [0]
changeList(list)
print(list)


def printKeyParam(name, age):
    print(name)
    print(age)
    return


printKeyParam(age=20, name="zhou")


def printDefaultParam(name, age=35):
    print(name, end=" ")
    print(age)
    return


printDefaultParam(name="zhou", age=50)
printDefaultParam(name="zhou")


def printVariableParam(argv, *varTuple):
    print(argv)
    for var in varTuple:
        print(var)
    return


printVariableParam(10, 20, 30, 40)
printVariableParam(10)


def printVarParam(argv, **varDict):
    print(argv)
    print(varDict)
    return


printVarParam(10, a=20, b=30)


def func(a, b, *, c):
    return a + b + c

print(func(1, 2, c=3))


sum = lambda argv1 , argv2 : argv1 + argv2
print(sum(20, 20))

total = 0;
def localVariate(a, b):
    global total
    total = a + b
    print(total)
    return total

localVariate(10,20)
print(total)


def outer():
    number = 10
    def inner():
        nonlocal number
        number = 100
        print(number)
    inner()
    print(number)

outer()

a = 10
def test():
    a = 10
    a = a + 1
    return a

print(a)
print(test())

