import sys

import importFileTest
from importFileTest import fab1
from importFileTest import fab2

for i in sys.argv:
    print(i)

print(sys.path)

importFileTest.fab1(1000)
print()
print(importFileTest.fab2(1000))

fab1 = importFileTest.fab1
fab2 = importFileTest.fab2
fab1(1000)
print()
print(fab2(1000))

print(dir(importFileTest))

