#！/usr/bin/python3
import sys

print("i'm %s and i'm %d years old " % ("x",1))

var={'a':'1','b':'2'}
print(var)
print(var['a'])
var['c']='3'
print(var)

a,b=0,1
while(b<10000):
	print(b,end=",")
	n=b
	m=a+b
	a=n
	b=m

print("")


a,b=True,False
if a and b:
	print("a and b are true")
elif a and b==False:
	print("a is true and b is false")
elif b and a==False:
	print("b is true and a is false")
else:
	print("a and b are both false")
	
	
# a=7
# b=0
# while(a!=b):
	# b=int(input("please input the number:"))
	# if(a<b):
		# print("<")
	# elif(a>b):
		# print(">")
	# else:
		# print("=")
# else:
	# print("=")


a=["c","c++","java","shell","python"]
for language in a:
	print(language)
	if(language=="java"):
		break


#scan with index
for i in (range(len(a))):
	print(i , a[i])


# for i in range(5):
for i in range(5,50,20):
	print(i)

#construct with iteritems
a=list(range(5))
print(a)

while(True):
	pass





