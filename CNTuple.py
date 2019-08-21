tup1 = 1, 2, 3, 4
tup2 = 'a', 'b', 'c','d'
tup3 = 'hello', 'world'
print(tup1, tup2, tup3)

tup1 = ()
print(type(tup1))

tup1 = (50)
print(type(tup1))

tup1 = (50,)
print(type(tup1))

for i in tup2:
    print(i)

print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3])
print(tup2[:])

tup1 = tup2 + tup3
print(tup1)

del (tup1)

print(len(tup2))
print((1, 2, 3) + (4, 5, 6))
print(('hi!',) * 4)
print(3 in (1, 2, 3))

print(tup2[2])
print(tup2[-2])
print(tup2[1:])

print(max(tup2))
print(min(tup2))
print(len(tup2))

list1 = [1, 2, 3, 4, 5]
print(type(tuple(list1)))

