from distutils import filelist
from re import T
import sys
import os
import stat

target = input('请输入需要遍历的目录：')
os.chdir(target)
#指定目录
def walkDir(path):
    with open('../DIR.txt','a')as f:
        for dirName, subdirList, fileList in os.walk(path):
            lead = dirName
            
            for fname in fileList:
                mass = lead+ '\\' + fname+'\n'
                str = mass.replace(target,'')
                str = str.replace('\\','/')
                if str[-4:] == '.js\n':
                    continue
                if str[-5:] == '.css\n':
                    continue
                if str[-5:] == '.jpg\n':
                    continue
                if str[-5:] == '.gif\n':
                    continue
                if str[-5:] == '.png\n':
                    continue
                f.write(str)

if __name__ == '__main__':
    walkDir(target)
    #   启动函数
    