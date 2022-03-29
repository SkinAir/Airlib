from ctypes.wintypes import WORD
import os
import threading
import queue

def air(test):

    words = queue.Queue()

    with open(test) as file:
        for i in file:
            i = i.strip()
            words.put(i)

    return words

def rad(zidian):
    while True:
        if zidian.empty():
            return
        else:
            i = zidian.get()
            i = i.strip()
            ml = ".\\rad.exe -t "+i+" --http-proxy 127.0.0.1:7777"
            os.system(ml)

def main():
    ac = air("iptables1.txt")
    threads = []
    for i in range(1):
        t = threading.Thread(target=rad,args=(ac,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        print("扫描结束...")

if __name__ == "__main__":
    main()