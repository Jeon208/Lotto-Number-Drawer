# Lotto Number Drawer
import random

#=============================================================#

# Logo
def l_message():
    print("""
██╗░░░░░░█████╗░████████╗████████╗░█████╗░
██║░░░░░██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗
██║░░░░░██║░░██║░░░██║░░░░░░██║░░░██║░░██║
██║░░░░░██║░░██║░░░██║░░░░░░██║░░░██║░░██║
███████╗╚█████╔╝░░░██║░░░░░░██║░░░╚█████╔╝
╚══════╝░╚════╝░░░░╚═╝░░░░░░╚═╝░░░░╚════╝░
""")
    
def s_message():
    print("""
░██████╗████████╗░█████╗░██████╗░████████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░
██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
""")
    
def d_message():
    print("""
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
██║░░██║██╔══██╗██╔══██║░░████╔═████║░
██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░
    """)

def c_message():
    print("""
░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
    """)


# Define 'lar_num'
def LNum():

    global lar_num
    lar_num = int(input("[!] The Largest number of balls *ex 50\n>> "))
    return lar_num

# Define 'ball_num'
def BNum():

    global ball_num
    ball_num = int(input("[!] The number of balls *ex 6\n>> "))
    return ball_num

# Define 'tries'
def Try():

    global tries
    tries = int(input("[!] Try number\n>> "))
    return tries

# Basic Start Menu
def Start():
    l_message()
    LNum()
    BNum()
    s_message()

# Draw and Print
def Draw():
    d_message()

    global lotto
    balls = range(1,lar_num+1)

    Try()

    for i in range(1,tries+1) :
        print("try :",i)
        
        lotto = random.sample(balls,ball_num)
        print(lotto,"\n")

# Just define 'lotto' to use in function 'Check()'
def Draw_np():
    global lotto
    balls = range(1,lar_num+1)
    lotto = random.sample(balls,ball_num)

# Check
def Check():

    c_message()

    global j
    j = 1
    global MyLotto
    MyLotto = []
    global same
    same = []
    score = 0

    # Define 'lotto'
    Draw_np()

    # Auto Draw Y/N
    ask = input("[*] Auto Draw (Y/N)\n>> ")

    # In Using Case
    if ask == 'Y' or 'y':
        # Repeat
        while j <= ball_num:

            MyNum = random.randrange(1, lar_num+1)
            print(f"\n[!] My Number {j}\n>> {MyNum}")

            # Normal Case
            if MyNum not in MyLotto:
                MyLotto.append(MyNum)

                # Plus Score
                if MyNum in lotto:
                    score += 1
                    same.append(MyNum)

            # Duplicational Case
            else:
                j -= 1

            j += 1

        # In Hand Case
        while j <= ball_num:

            MyNum = int(input(f"\n[!] My Number {j}\n>> "))
            MyLotto.append(MyNum)

            if MyNum in lotto:
                score += 1
                same.append(MyNum)
            j += 1
    same.sort()

    print(f"""

LOTTO : {lotto}
    
My Lotto : {MyLotto}

SCORE : {score}/{ball_num} -- {same}

    """)

#=============================================================#


Start()

print("[#] Mode 'D' draws lottery many times.")
print("[#] Mode 'C' checks my lotto and lotto")
print()
mode = input("[~] Select Mode (D/C)\n>> ")

# Mode
if mode in ['d', 'D']:
    Draw()
else:
    Check()

print("\nDone\n")
