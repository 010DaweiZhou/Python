
score  = int(input("input :"))

if score >= 90:
    print('A')
else:
    if score >= 70:
        print('B')
    else:
        if score >= 60:
            print('C')
        else:
            print('D')


if 100 >= score >= 90:
    print('A')
elif 90 >= score >= 70:
    print('B')
elif 70 >= score >= 60:
    print('C')
else:
    print('D')

x = 1 
y = 2

a = x if x < y else y
print(a)

# assert x > y

x = y

i = 0
while i<100 :
    if i == 50:
        break
    i += 1

print(i)

i = 0
for i in range(0,5,1):
    if i== 2:
        break
    print(i)


for i in range(0,10,1):
    if i == 5:
        continue 
    print(i ,end = " ")

