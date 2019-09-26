
import json

data = {
    'no': 1,
    'name': 'cainiao',
    'url': 'http://www.baidu.com',
    'list': [1, 2, 3, 4, 5, 6]
}


j = json.dumps(data)
print(j)
print(repr(data))

new_data = json.loads(j)

print(new_data)

with open('data.json', 'w') as f:
    f.write(json.dumps(data))

del data
del new_data
del j

with open('data.json', 'r') as f:
    print(json.load(f))


