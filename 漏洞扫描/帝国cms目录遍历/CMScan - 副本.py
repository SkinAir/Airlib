import threading
import requests
from queue import Queue
import random
from colorama import Fore, Back, Style

#目录遍历
class Dirscan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()    
            try:
                with open("result.txt",'w')as F:
                    headers = {
                        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                    }
                    #发送请求
                    res = requests.get(url=url,headers=headers)
                    if res.status_code == 200:
                        success ="[+] Success is %s : 200 " % url
                        print(Fore.GREEN + success)
                        #写入文件
                        F.write(success)
                    elif res.status_code !=200 :
                        fail = Fore.RED + "[-] Fail is %s : %d" % (url,res.status_code)
                        #print(fail)
                        F.write(fail)
            except Exception as e:
                print("主机拒绝连接")

#启动项
def start(url,web,count):
    queue = Queue()

#引用目录文件
    with open("%s.txt" % web, "r")as f:
        for i in f:
            newUrl = url + i.strip('\n')
            queue.put(newUrl)

    threads = []
    thread_conut = int(count)
#多线程
    for i in range(thread_conut):
        threads.append(Dirscan(queue))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    url = "http://192.168.31.132/"
    web = "DIR"
    count = 50
    start(url, web, count)