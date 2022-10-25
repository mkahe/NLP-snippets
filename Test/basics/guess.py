import random

answer = random.randint(1,10)

while True:
    x = int(input("Enter a number: "))
    if x == answer:
        print("HOORAY!! You won!")
        break
    if x > answer:
        print("Your number is bigger")
    else:
        print("Your number is smaller")
    
