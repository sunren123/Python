import threading
import time

def saySorry():
    print("我真的错了！！")
    time.sleep(1)



if __name__ == '__main__':
    for i in range(15):
        t= threading.Thread(target=saySorry())
        t.start()