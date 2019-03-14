#!/usr/bin/python3
a=10
b=10

print(a==b)
a+=b;
print(a)

#now a=20
a//=b;
print(a)

a=3
b=1
#2
print(a^b)
#1
print(a&b)
#3
print(a|b)
#3*2
print(a<<b)
#3//2
print(a>>b)

a=True
b=False

print(a and b)
print(a or b)
print(not a)

#create a list
a=[1,2,3,4]
print(1 in a)
print(5 not in a)

#create a tuple
a=(1,2,3,4)
print(5 in a)

#create a set
a={1,2,3,4}
print(5 in a)
print(5 not in a)

#use dict
a={}
a=dict([(1,2),(2,3),(3,4)])
print(a)

a=1
b=1
print(a is b)
print(a==b)

a=0xff
print(a)

a=0o77
print(a)

print(10.0/3)
print(10.0//3)




