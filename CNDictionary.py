a = {'name': "zhou",
     'age': 20,
     'sex': 'man'
     }
print(a)

print(a['name'])
print(a['age'])
print(a['sex'])

a['name'] = 'jay'
a['country'] = 'china'
print(a)

del a['name']
print(a)

a.clear()
print(a)

del a

a = {1: 2,
     3: 4,
     5: 6,
     (5,6): 7}

print(a)
# a[[1, 2]] = 8
# print(a)

print(len(a))
print(type(a))

b = a.copy()
print(b)

del b
b = {}
b = b.fromkeys((1, 2, 3))
print(b)
b = b.fromkeys((1, 2, 3) , 10)
print(b)

print(1 in b)
x = b.keys()
print(x)
for i in x:
     print(i)

x = b.items()
print(x)
for i in x:
     print(i)

x = b.keys()
print(x)
for i in x:
     print(i)

b.setdefault(4, 10)
print(b)

b2 = {5: 10, 6: 10}
b.update(b2)
print(b)

x = b.values()
print(x)
for i in x:
     print(i)

x = b.pop(5)
print(b , x)

b.popitem()
print(b)

