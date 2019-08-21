list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = ['google', 'runnoob', 1997, 2000]

print(list1[0])
print(list3[:])

list1.append(5)
print(list1)

list1[0] = 100
print(list1)

del list1[0]
print(list1)

print(len(list1))
print([1, 2, 3] + [4, 5, 6])

print('hello\n' * 4)

if 1 in [1, 2, 3]:
    print('hello world!')

for x in [1, 2, 3]:
    print(x)

print(list1[2])
print(list1[-2])
print(list1[1:])

w = [1, 2, 3]
c = [4, 5, 6]
a = [w, c]
print(a)
print(a[0][1])

print(max(a))
print(min(a))

print(max(w))
print(min(w))
print(max(c))
print(min(c))

print(len(w))
print(len(a))

a = 1, 2, 3
b = list(a)
print(b)
print(b.count(1))
b.extend([4, 5])
print(b)
print(b.index(1))
b.insert(0, 100)
print(b)
print(b.pop())
b.remove(4)
print(b)

a = b.copy()
print(a)

b.reverse()
print(b)

b.sort()
print(b)

b.clear()
print(b)








