import os
print("\nHello! Made With Love By Sakshi, Bhuvan and Kunal\n")
while True:
    print("Choose Your Option:")
    print("1.Volume Control Using Hand Gesture")
    print("2.Mouse Control Using Hand Gesture")
    print("3.Exit")
    p = int(input())
    if(p!=1 or p!=2):
        if(p==1):
            exec(open('Volume_Control.py').read())
        elif(p==2):
            exec(open('Mouse_Control.py').read())
        elif(p==3):
            break
        else:
            print("Invalid Entry")


