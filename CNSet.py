import sys

basket1 = {'apple', 'banana', 'orange', 'pear', 'apple'}
basket2 = {'apple', 'banana', 'orange', 'pear', 'watermelon'}

for item in basket1:
    print(item)

print('apple' in basket1)


basket = basket1 | basket2
print(basket)

basket = basket1 & basket2
print(basket)

basket = basket1 - basket2
print(basket)

basket = basket1 ^ basket2
print(basket)

a = {x for x in 'abcdefg' if x not in 'abc'}
print(a)
del a

a = set()
for x in 'abcdefg':
    if (x not in 'abc'):
        a.add(x)

print(a)

if('g' in a):
    a.remove('g')
    print(a)

a.discard('d')
print(a)

a.pop()
print(a)

print(len(basket))
a.clear()
print(a)


a, b = 0, 1

while (b < 100):
    print(b, end = ',')
    a, b = b, a + b

print()
a = 1
while a < 10:
    if (a % 2 == 0):
        print('%d is even' % a)
    else:
        print('%d is odd' % a)
    a += 1


a = int(input('value:'))
if a < 10:
    print('a < 10')
elif a < 20:
    print('a < 20')
else:
    print('a >= 20')

if 1:
    if 2:
        print(2)
    elif 3:
        print(3)
    elif 4:
        print(4)
    else:
        print(5)
else:
    print(6)

a = 0
while a < 10:
    print(a)
    a += 2

a = 100
result = 0
while a > 0:
    result += a
    a -=1

print(result)

def sum(x):
    if (x == 1):
        return 1
    else:
        return x + sum(x - 1)
        
print(sum(100))

count = 10
while count >= 5:
    print(count , 'ge')
    count -= 1
else:
    print(count , 'l')

for i in range(5):
    print(i)
    if (i == 3):
        break
else:
    print(0)

a = ['a', 'b', 'c', 'd', 'e']

for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))

for i in range(5,10):
    pass

list1 = [1, 2, 3, 4]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for x in iter(list1):
    print(x)

it = iter(list1)

while True:
    try:
        print(next(it))
    except StopIteration :
        sys.exit()

