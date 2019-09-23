
import re

# match from start of string
result = re.match(r'(\d+)(\w)', '123a', 0).group()
print(result)
result = re.match(r'(\d+)(\w)', 'a123a', 0)
print(result)

# search in all string
result = re.search(r'(\d+)(\w)', '123a', 0).group()
print(result)
result = re.search(r'(\d+)(\w)', 'a123a', 0).group()
print(result)


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


str1 = 'hello, here is http://www.baidu.com:8080'
result = re.search(r'(\w+)\:\/\/([^\:]+)\:(?P<port>\d+)', str1, 0)
print(result)

new = re.sub(r'(\w+)\:\/\/([^\:]+)\:(\d+)', 'www.taobao.com:8392', str1)
print(new)

new = re.sub(r'(?<=\:)(?P<value>\d+)', double, new)
print(new)

pattern = re.compile(r'(?P<str>\w+?)(?P<num>\d+)', re.M | re.I)
result = pattern.search('aas12361236')
print(result.groups())
start = result.start('str')
end = result.end('num')
print(start, end)

pattern = re.compile(r'\d+')
result = pattern.findall("ass1236www9966www6379")
print(result)






