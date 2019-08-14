import random

value = random.randint(1,10)

while(1):
    temp = input("you guess number:")
    guess = int(temp)
    
    if guess == value:
        print("right!")
        break
    else:
        if guess > value:
            print("too big !")
        if guess < value:
            print("too small !")

print("end , bye!")
