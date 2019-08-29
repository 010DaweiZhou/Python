from collections import deque
import sys


class MyNumber:

    a = 0

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumber()

for i in myclass:
    print(i, end=' ')
print()

myit = iter(myclass)

for i in myit:
    print(i, end=' ')
print()


def fib(x):
    a = 0
    b = 1
    count = 0
    while count <= x:
        yield a
        a, b = b, a + b
        count += 1


f = fib(20)

for i in f:
    print(i, end=' ')

print()

list1 = [1, 2, 3, 4, 5]
list1.extend([1, 2, 3, 4])
print(list1)

if 6 in list1:
    list1.remove(6)

list1.pop()
print(list1)

del list1

list1 = [1, 2, 3, 4, 5]
list1.append(6)
print(list1.pop())


queue = deque([1, 2, 3, 4])
queue.append(5)
print(queue.popleft())

vec = [1, 2, 4]
for i in vec:
    print(i * i, end=' ')
print()

result = [x * x for x in vec]
print(result)

freshfruit = ['  apple', 'banana   ', '  pear  ']
print([i.strip() for i in freshfruit if len(i.strip()) > 5])

vec1 = [1, 3, 5, 7]
vec2 = [2, 4, 6, 8]
print([x * y for x in vec1 for y in vec2])
print([x + y for x in vec1 for y in vec2])
print([vec1[i] * vec2[i] for i in range(len(vec1))])

vec3 = [
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]
]

print([[per[i] for per in vec3] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([per[i] for per in vec3])
print(transposed)

a = [1, 2, 3, 4, 5]
del a[0]
print(a)

del a[:2]
print(a)

del a[:]
print(a)

t = 1, 2, 3, 4
n = t, (5, 6, 7, 8)
print(n)

dict1 = dict([(1, 2), (3, 4)])
print(dict1)
print(dict1[1])

dict2 = {x: x * x for x in range(4)}
print(type(dict2), dict2)

for a, b in dict1.items():
    print(a, b)

print(dict(a=1, b=2, c=3))

for a, b in enumerate([1, 2, 3]):
    print(a, b)



for i in range(1, 10, 2):
    print(i ,end = ' ')

print()
for i in reversed(range(1, 10, 2)):
    print(i, end=' ')


