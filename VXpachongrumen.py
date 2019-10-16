
from bs4 import BeautifulSoup
import requests
namebook = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(namebook)

for key, value in namebook.items():
    print(key, value)

a = 10

if a == 1:
    print('a')
elif a == 2:
    print('b')
else:
    print('c')


def caculate(x):
    y = x + 1
    return y


print(caculate(1))


class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def p(self):
        print(self.name + ' ' + str(self.age))


zhou = Person('zhou', 20)
zhou.p()


class Zhou(Person):

    def __init__(self, name, age, property):
        Person.__init__(self, name, age)
        self.property = property

    def detail(self):
        print(self.name)


del zhou
zhou = Zhou('zhou', 20, 'handsome')
zhou.detail()

link = 'http://www.santostang.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Host' : 'www.santostang.com'}
result = requests.get(link, headers)

soup = BeautifulSoup(result.text, 'lxml')
title = soup.find('h1', class_='post-title').a.text.strip()

with open('result.txt', 'w+', encoding='utf-8') as f:
    f.write(title)

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%2d' % (j, i, i * j), end=' ')
    print('')

r = requests.get('http://www.santostang.com')
print(r.encoding)
print(r.status_code)
del r
param = {'key1':'value1','key2':'value2'}
r = requests.get('http://httpbin.org/get', params=param)
print(r.status_code)
print(r.url)
print(r.text)

del r
r = requests.post('http://httpbin.org/post', data=param)
print(r.status_code)
print(r.text)

