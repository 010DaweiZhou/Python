
import sys
import random

argList = ['a.txt', 'b.txt', 'c.txt', 'test.txt']


for arg in argList:
    try:
        file = open(arg, 'r')
    except IOError:
        print('can\'t open ', arg)
    else:
        print('open success!')
        result = file.read()
        try:
            i = int(result)
        except ValueError:
            print('can\'t convert to int !')
        else:
            print('close file now!')  
            file.close()

for i in range(10):
    rand_value = random.randrange(0, 10)
    x = 10
    try:
        print('%.3f' % (x / rand_value))
    except ZeroDivisionError:
        print('zero can\'t be divided!')


class MyException(Exception):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr('my exception occurred!, value :', self.value)
        
try:
    raise MyException(4)
except MyException as e:
    print(e.value)

# try:
#     raise KeyboardInterrupt
# finally:
#     print('hello world!')

with open('test.txt') as file:
    for line in file:
        print(line ,end = '')



