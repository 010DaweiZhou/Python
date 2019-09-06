import os

print(os.getcwd())
# os.chdir("D:\\")
# print(os.getcwd())

# os.system('mkdir xxx')
os.system('dir')

print(dir(os))
# print(help(os))
 
import glob
print(glob.glob('*.py'))

import shutil
shutil.copyfile('test.txt', 'test2.txt')
shutil.move('test2.txt', 'test1.txt')

import sys
print(sys.argv)

print('tea for too'.replace('too', 'two'))

import math
print(math.cos(math.pi / 4))
print(math.sin(math.pi / 2))

import random

print(random.randint(0, 100000000))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random.random())
print(random.sample(range(100), 10))
print(random.randrange(0, 6, 1))

# from urllib.request import urlopen
# for line in urlopen(r'http://www.baidu.com'):
#     line = line.decode('utf-8')

from datetime import date
now = date.today()
print(now)

birthday = date(1996, 4, 13)
print(now - birthday)

import zlib
s = 'hello i am kangkang and i\'m from china'.encode('utf-8')
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t).decode('utf-8'))
print(zlib.crc32(t))

from timeit import Timer
print(Timer('t = a ; a = b ; b = t', 'a = 1 ; b= 2').timeit())
print(Timer('a , b = b ,a', 'a = 1 ; b= 2').timeit())

def average(values):
    """
    >>> print(average([20,30,70])) 
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()

import time

time_stamp = time.time()
print(time_stamp)
