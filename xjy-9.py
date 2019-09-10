
#!/usr/bin/python

try:
    file = open('x.txt', 'r')
    for line in file:
        print(line)
except FileNotFoundError:
    print('file not found.')

mylist = [1]
assert len(mylist)
# mylist.pop()
# assert len(mylist)


try:
    value = 1 + '1'
except TypeError:
    print('type error!')

mylist.append(2)
try:
    print(mylist[3])
except IndexError:
    print('index error!')

try:
    mylist.addd()
except AttributeError:
    print('error attribute!')


mydir = {1: 2, 3: 4}
try:
    print(mydir[4])
except KeyError:
    print('key not found!')

try:
    print(a)
except NameError as reason:
    print('a is not found! %s' % reason)

try:
    a = '1' / 0
except (ZeroDivisionError, TypeError):
    print('error!')


try:
    file = open('x.txt', 'r')
    a = 1/ 0
except (FileNotFoundError , ZeroDivisionError):
    print('error!')
finally:
   pass

# raise ZeroDivisionError

i = 0
while i < 10:
    i += 1
    break
else:
    print('else' + str(i))
print(i)


try:
    abc = int('abc')
except (ValueError, TypeError ) :
    print('error! ')
else:
    print('no error!')

try:
    with open('t.txt', 'r') as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print('no file existed!')



    



