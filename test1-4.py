#!/usr/bin/python3
import sys

print("hello world!",end=" ")

'''
	xxx
'''

if True:
	print\
	("xxx")
	print("yyy")
	
print(r"hello!\n");print("""hello
world!""" + "!"*2)

x="hello"
sys.stdout.write(x+"\n")

print(sys.path)

a=b=c=1
a,b,c=1,1.0,1.00
d=1+2j

print(a+b+c+d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(isinstance(a,int))

print(a//b)

del a,b,c,d

a="hello world!"
print(a[0:-1])
print(a[0])


#list[]
a=["a","b","c",1,2,3.0]
print(a[0:-1])
print(a[0]*2+a[1])
a[0]=1
print(a[0:])
a[0:2]=[3,3]
print(a[0:])

#sum
print(a[0]+a[1]) 

print(a[0:3:2])

del a

#tuple()
a=(1,2,3,"a","b","c")
print(a)
print(a[0:-1])

#sum
print(a[0]+a[1])

#set use {} 
#but when the set is null must use set()
#beacuse {} is used for creating a dict
a={1,1,1,2,2,3,3}
print(a)
if 1 in a:
	print(True)
else:
	print(False)
a=set("abcdefg")
b=set("abcdefghijklmn")

print(a-b)
print(a|b)
print(a&b)
print(a^b)

#create a null dictionary
dict={}

dict["one"]="hello"
dict[2]="world"
dict["3"]="world"
print(dict)

a=1
b=str(a)
print(type(b))
del a

#just use for one char , if a = 10 , b will be "10" , ord(b) will be wrong
a=ord(b)
print(type(a))
del b



#input("\ninput enter to exit...")
