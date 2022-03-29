from ast import arg
import threading
import requests
from queue import Queue
import random
from colorama import Fore, Back, Style
import argparse


#目录遍历
class Dirscan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()    
            try:
                headers = {
                    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                }
                #发送请求
                res = requests.get(url=url,headers=headers)
                if res.status_code == 200:
                    print(Fore.GREEN + "[+] Success is %s : 200 " % url)
                elif res.status_code !=200 :
                    print(Fore.RED + "[-] Fail is %s : %d" % (url,res.status_code))
            except Exception as e:
                print("主机拒绝连接")

#启动函数
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

#定义命令行参数
def parse_args():
    #创建解析对象
    parser = argparse.ArgumentParser()
    #添加命令
    parser.add_argument("-u","--url",help="Specify your URL")
    #解析复制给args
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    url = str(args.url)
    web = "DIR"
    count = 50
    start(url, web, count)