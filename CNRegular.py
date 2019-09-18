
import re
result = re.match('www' , 'www.baidu.com' , 0)
# result = re.match('wwww' , 'www.baidu.com' , 0)
print(result)

str1 = 'abc1234jqk'
result = re.match(r'^[a-z]+[0-9]+[a-z]+$', str1, 0)
print(result)

email = 'david_zhou@gmail.com'
result = re.match(r'^[0-9a-zA-Z_]{6,15}@[0-9a-z]+.com', email, 0)
print(result)

str1 = 'runoooooooooooooooooob'
result = re.match(r'runo+b', str1, 0)
print(result)
result = re.match(r'runo*b', str1, 0)
print(result)
# result = re.match(r'runo?b', str1, 0)
# print(result)

str1 = 'runbooooo*b'
result = re.match(r'runbo+\*b$', str1, 0)
print(result)

result = re.match(r'^r.*?b', str1, 0)
print(result)

str1 = 'good good study , day day up!'
result = re.match(r'\b([a-z]+) \1\b', str1, 0)
print(result)

import os
count = 0
print(os.getcwd())
allfiles = list(os.walk('.'))
for root,dirs,files in allfiles:
    for filename in files:
        if re.match(r'.*\.py$', filename, 0):
            print(filename)
            with open(filename, 'r' ,encoding='utf-8') as file:
                for line in file:
                    if re.match('^\n', line, 0):
                        continue
                    count += 1
            file.close()
print('count total = %d' % count)

result = re.match(r'[a-z]','g',0)
print(result)

result = re.match(r'[^a-z]','g',0)
print(result)

result = re.match(r'^(?:C|S) [1-9][0-9]{0,1}','C 1',0)
print(result)

result = re.findall(r'(\w+):\/\/([^\:]+)(:\d*)?([^#]*)','http://www.baidu.com:8080',0)
print(result)

result = re.findall(r'Windows(?=95|98|2000)','Windows95Windows98Windows2000Windows10',0)
print(result)

