import sys

sys.setrecursionlimit(1000)

def myFirstFunction():
    print("hello")
    print("world!")
    return


myFirstFunction()

for i in range(3):
    myFirstFunction()


def mySecondFunction(name):
    print(name)
    return


mySecondFunction("hello !")


def add(a, b):
    ''' a add b'''
    return a + b


print((add(1, 2)))

print(add.__doc__)
print(help(add))


def helloWorld(name='java', do='++'):
    return name + '->' + do


print(helloWorld('c', '++'))

print(helloWorld(do='++', name='java'))
print(helloWorld())


def collectParam(* param, default='c'):
    print('there are %d param' % len(param))
    print('default param is %s ' % default)


collectParam('a', 'b')


def test(*param):
    print('%d ' % len(param))
    print(param[1])


a = [1, 2, 3, 4, 5]
test(*a)


def multiReturn():
    return 1, 2, 3, 4


print(multiReturn())

old_price = 80
rate = 0.5

def discounts(price, rate):
    global old_price 
    old_price = 50
    print('old price %d' % old_price)
    final = price * rate
    return final

new = discounts(old_price,rate)
print('old price = %d' % old_price)
print('new = %d ' % new)

def fun1():
    print('func 1 is running...')
    def fun2():
        print('func 2 is running...')
    fun2()

fun1()

def funX(x):
    def funY(y):
        return x * y
    return funY

i = funX(8)
print(i(5))

print(funX(5)(10))

def funZ(x):
    x = 5
    def funY(y):
        nonlocal x 
        x = x * y
        return x 
    return funY


print(funZ(2)(3))

g = lambda x : x * x + 1
print(g(5))

add = lambda a ,b : a+b
print(add(1,2))

temp = filter(None , [0,1,2,3,4])
print(list(temp))

def odd(x):
    return x % 2
'''pass the values who can % 1'''
temp = filter(odd,range(10))
print(list(temp))

temp = filter(lambda x : x % 2 , range(10))
print(list(temp))

temp = map(lambda x : x * x , range(10))
print(list(temp))

def recursion(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

print(recursion(4))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))

def fab(x):
    a1 = 1
    a2 = 1
    a3 = 1

    if x < 1:
        print('error!')
        return -1
    
    while(x - 2) > 0:
        a3 = a1 + a2 
        a1 = a2 
        a2 = a3 
        x -= 1
    return a3

print(fab(10))

def new_fab(x):
    if x < 1:
        return -1
    
    elif n == 1 or n == 2:
        return 1
    else:
        return fab(x-1) + fab(x-2)

print(fab(10))




