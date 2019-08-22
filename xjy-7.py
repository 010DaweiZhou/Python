import sys

empty = {}
print(empty)

dict1 = dict(((1, 2), (3, 4), (5, 6), (7, 8)))

for i in dict1.values():
    print(i, end=' ')

print()

for i in dict1.keys():
    print(i, end=' ')

print()

dict1 = dict.fromkeys((1, 2, 3, 4), 1)
print(dict1)

items = dict1.items()
print(items)

print(dict1.get(2))

print(dict1.get(5, "no"))

print(2 in dict1)

dict2 = dict1
dict1 = {}
print(dict1)
print(dict2)

dict1 = dict2
dict1.clear()
print(dict1)
print(dict2)

del dict2
dict1 = dict(a=1, b=2, c=3, d=4)
print(dict1.pop('a'))
print(dict1.popitem())
print(dict1)

dict1.setdefault('e', 5)
print(dict1)

dict1.update({'f': 6})
print(dict1)


def test1(**param):
    print('len %d' % len(param))
    print(param)


test1(a=1, b=2, c=3)
test1(**dict1)

set1 = {1, 2, 3, 4, 1, 2, 3, 4}
print(type(set1))
for i in set1:
    print(i ,end = " ")
print()

set2 = set([1,2,3,4])
print(set1 == set2)

set1.add(5)
set2.add(5)
print(set1 == set2)

set1.remove(1)
print(set1)

set1 = frozenset([1,2,3,4,5])



