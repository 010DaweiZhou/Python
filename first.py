import random
import sys

# x = random.randint(1, 100)
# guess = 0

# while guess != x:
#     temp = input('你猜我想的啥？\n')
#     guess = int(temp)

#     if guess != x:
#         print("垃圾!")

#     if guess < x:
#         print("小了！")
#     else:
#         print("大了！")

# print("666！")

x = "hello\'"
y = "world!"
print(x + y)

for i in range(0, 10, 2):
    print(i)

number = [1, 2, 3, 4, 5]

#insert a value
number.append(6)

#insert multiple value
number.extend([7, 8])

#insert a value at one specified position
number.insert(0,0)
print(number)

#change the position
number[0] , number[3] = number[3], number[0]
print(number)

#delete a specified value , if it's not existed , throw error
number.remove(1)
print(number)

#pop the last value
number.pop()
number.pop()
print(number)

#pop the first one
number.pop(0)
print(number)

#list slice
print(number[0:2])

#inverse
print(number[::-1])

#count of value in the list
print(number.count(1))

#find the position of value in the list
print(number.index(5))
start = number.index(5) + 1 
end = len(number)
# print(number.index(5,start,end))

#sort from big th small
number.sort(reverse = True)
print(number)

#delete the list
del number

