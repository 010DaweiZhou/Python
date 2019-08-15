
a = []
a = [1, 2, 3, 4, 5]
a = [1, 1.1, 'a', "abc"]

print(a)

a.append(2)
print(a)

a.extend([7, 8])
print(a)

a.insert(0, 'hello')
print(a)

a[0], a[1] = a[1], a[0]

print(a)

a.remove(1)
print(a)

del a[1]
print(a)


a.pop(0)
print(a)

print(a[0:2])
print(a[::-1])

print(a[:2] + a[2:])
print(a * 2)
for i in a:
    print(i)

print(2 in a)
print(2 not in a)

a.append([3, 4])
print(a)

print(a[5][0])

print(a.count(3))
print(a.count(2))
print(a.index(2))

a.reverse()
print(a)

a = [1, 2, 3, 4, 6, 5]
a.sort()
print(a)
a.reverse()
print(a)

b = (1, 2, 3, 4, 5, 7, 6)
print(b)

for i in b:
    print(i)

b = (1)
print(type(b))

b = (1,)
print(type(b))

b = (1, 2, 4, 5, 6)
b = b[:2] + (3,) + b[2:]
print(b)

str = 'hello world!'
str = 'zhou, ' + str
print(str)

str = str.capitalize()
print(str)

print(str.count('o'))

str = " ".join(['i', 'love', 'you'])
print(str)
str = str.split(sep=' ')
print(str)

str = "{0} love {1}".format('i', 'love')
print(str)

str = "%#x" % 1000
print(str)

a = list((1, 2, 3, 4, 5))
print(a)

a = (1, 2, 3, 4, 5)

b = list()
for i in a:
    b.append((i))

print(b)

b = tuple(b)
print(b)

length = len(b)
print(length)

max = max(b)
print(max)

min = min(b)
print(min)

tuple = 1,2,3,4,5
sum = sum(tuple)
print(sum)


for i in reversed(tuple):
    print(i , end =  ",")

print('')


a = 1,2,3,4,5
b = 'a','b','c','d','e'

for each in zip(a,b):
    print(each)

for each in enumerate(b):
    print(each)

