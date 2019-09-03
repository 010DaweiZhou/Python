
str1 = 'hello world!'

print(str1)
print(repr(str1))

print(str(1 / 7))

str1 = 'hello world!\n'
print(str1)
print(repr(str1))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print('-3.14'.zfill(7))
print('{} website:{}'.format('baidu', 'www.baidu.com'))
print('{0} website:{1}'.format('baidu', 'www.baidu.com'))
print('{1} website:{0}'.format('baidu', 'www.baidu.com'))
print('{name} website:{address}'.format(name='baidu', address='www.baidu.com'))
print('{0} website:{1} , {other}'.format('baidu', 'www.baidu.com', other='hello world!\n'))

table = {'google': 1, 'baidu': 2, 'taobao': 3}
print('{0[google]:d} {0[baidu]:2d} {0[taobao]:3d}'.format(table))
print('{google:d} {baidu:2d} {taobao:3d}'.format(**table))

import math
print('%.10f' % math.pi)

# str = input('please input: ')
# print(str)

file = open('test.txt', 'w+')

for i in range(100000):
    file.write('  ipv6 route 9999::' + str(i) + '/128 blackhole\n')

file.close()

dis = open('test.txt', 'w')
scr = open('CNFunc.py', 'r')

line = 'hello!'
while (line):
    line = scr.readline()
    dis.write(line)


scr.seek(0)
print(scr.read())


scr.seek(0)
for line in scr:
    print(line)


scr.seek(0)
line = 'hello'
count = 0
while line:
    line = scr.readline()
    count += 1
print('line total:' , count)


dis.close()
scr.close()


dis = open('test.txt', 'w')
tuple1 = (1, 2, 3, 4, 5)
dict1 = {1: 2, 3: 4, 5: 6, 7: 8}
dis.write(repr(tuple1) + '\n')
dis.write(repr(dict1) + '\n')
dis.write(str(tuple1) + '\n')
dis.write(str(dict1) + '\n')
print(dis.tell())
dis.close()

with open('test.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        print(i, end='')

print(f.closed)


import pickle
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dict1 = {   1: 1,
            2: 2,
            3: 3,
            4: 4}

file = open('data.pkl', 'wb')
if (file.writable()):
    pickle.dump(list1, file, -1)
    pickle.dump(dict1, file, -1)
file.close()

del list1
del dict1

file = open('data.pkl', 'rb')
if (file.readable()):
    list1 = pickle.load(file)
    dict1 = pickle.load(file)

if (list1 and dict1):
    print(list1, dict1)
file.close()

try:
    file = open('test.txt', 'w+')

    if file.writable():
        for i in range(10):
            file.write(str(i) + '\n')

    if file.readable():
        lines = file.readlines()
        for line in lines:
            print(line, end='')
        print(file.tell())

        file.seek(0)
        print(file.tell())

        file.seek(0,2)
        print(file.tell())

    file.truncate(6)
    print(file.read())

finally:
    file.close()



