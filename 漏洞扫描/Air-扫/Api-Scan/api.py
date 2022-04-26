
#!/usr/bin/env python
# coding:utf-8

from cgi import test
from importlib.resources import path
from urllib import response
import requests,sys,colorama
from colorama import *
import sys

banner = '''\033[1;33;40m
   _____ __________.___ 
  /  _  \\______   \   |
 /  /_\  \|     ___/   |
/    |    \    |   |   |
\____|__  /____|   |___|
        \/              
Have fun. Don't forget t
'''

def examples():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    with open(r'C:\Users\28564\Desktop\python-exp\ms-T\Exp.txt','r')as f:
        payload = f.readlines()
    # payload = '/swagger/index.html'
    # poc = urls + payload
    try:
        requests.packages.urllib3.disable_warnings()
        for exp in payload:
            exp = exp.strip('\n')
            response = requests.get(urls+exp, headers=headers, timeout=15,verify=False)
            if response.status_code == 200:
            #if response.status_code == 200:
                print(u'\033[1;31;40m[+]{} is may exists'.format(urls))
                print(response.text)
                with open('./APIresult.txt','a') as f:
                    f.write('[+]' + urls + exp)
                    f.write('\n')
            else:
                print('\033[1;32;40m[-]None: {}'.format(urls)+ exp)
    # except:
    #     print('{} request timeout'.format(urls))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    try:
        print(banner)
        path=sys.argv[1]
        if len(sys.argv) != 2:
            print('Example:python3 api.py urls.txt')
        else:
            with open(path , 'r') as u:
                line = u.readlines()
                for url in line:
                    urls = url.strip()
                    if urls[-1] == '/':
                        urls = urls[:-1]
                    examples()
                print('over')
    except Exception as e:
        print(e)
    # except:
    #     print('python3 api.py url.txt')
    #     sys.exit()


                

