import threading
import time

#use for background test ,garbage collection , waiting for input , long running process

def timer():
    print()
    count=0
    while True:
        time.sleep(1)
        count+=1
        print("logged in for : ",count,"seconds")

x = threading.Thread(target=timer,daemon=True)
x.start()

answer = input("Do you want to exit ? (Yes or No):"+"\n")

