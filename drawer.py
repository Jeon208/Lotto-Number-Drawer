# Lotto Number Drawer
import random



num = int(input("[!] largest number of balls *ex 50\n>> "))

num2 = int(input("[!] the number of balls *ex 6\n>> "))

tries = int(input("[!] try number\n>> "))

balls = range(1,num+1)


for i in range(1,tries+1) :
    print("try :",i)
    print(random.sample(balls,num2))
    print()
