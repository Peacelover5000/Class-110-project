import random
print("Press P to start playing, n to stop")
Play = input("Enter the input: ")
P=str
n=str
no = random.randint(1,6)
if( Play == P):
    print("Starting the Game!!!")
    print(no)

if( no == 1):
        print("[_________]")
        print("[         ]")
        print("[    0    ]")
        print("[         ]")
        print("[_________]")

if( no == 2):
        print("[_________]")
        print("[         ]")
        print("[ 0     0 ]")
        print("[         ]")
        print("[_________]")

if( no == 3):
        print("[_________]")
        print("[ 0       ]")
        print("[    0    ]")
        print("[       0 ]")
        print("[_________]")

if( no == 4):
        print("[_________]")
        print("[ 0     0 ]")
        print("[         ]")
        print("[ 0     0 ]")
        print("[_________]")

if( no == 5):
        print("[_________]")
        print("[ 0     0 ]")
        print("[    0    ]")
        print("[ 0     0 ]")
        print("[_________]")

if( no == 6):
        print("[_________]")
        print("[ 0     0 ]")
        print("[ 0     0 ]")
        print("[ 0     0 ]")
        print("[_________]")

elif( Play == n):
    print("Stopped the Game!!!")
