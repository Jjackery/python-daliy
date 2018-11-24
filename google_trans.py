# -*- coding: utf-8 -*-
import re
import urllib,urllib2
import HTMLParser
import os,threading

agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}

def unescape(text):
    parser = HTMLParser.HTMLParser()
    return (parser.unescape(text))

def TranslateByGoogle(text, fromLang="auto", toLang="zh-CN"):
    base_link = "http://translate.google.cn/m?hl=%s&sl=%s&q=%s"
    text = urllib.quote_plus(str(text))
    link = base_link % (toLang, fromLang, text)
    request = urllib2.Request(link, headers=agent)
    try:
        raw_data = urllib2.urlopen(request).read()
        data = raw_data.decode("utf-8")
        expr = r'class="t0">(.*?)<'
        re_result = re.findall(expr, data)
        if (len(re_result) == 0):
            result = ""
            print result
        else:
            result = unescape(re_result[0])
            print result
            result = result.encode('utf-8')
            new_file = open(path+"/"+file,'w')
            new_file.write(result)
            new_file.close()
        #return (result)
    except Exception, e:
        print e

def handle_txt():
    global path
    global file
    path = r"C:\Users\Administrator\PycharmProjects\untitled2\txt" #文件夹目录可以自己修改
    files= os.listdir(path)
    for file in files: #遍历文件夹
        if not os.path.isdir(file):
            f = open(path+"/"+file)
            iter_f = iter(f)
            str = ""
            for line in iter_f:
                str = str + line
                TranslateByGoogle(text=str)
    print '---翻译完成---'

def split_txt():
    with open(r'C:\Users\Administrator\PycharmProjects\untitled2\en.txt','r')as f:
        lines = f.readlines()
    for index,line in enumerate(lines,1):
        print(index,line)
        with open(r'C:\Users\Administrator\PycharmProjects\untitled2\txt\ch%d.txt' %index,'w+')as tmp:
            tmp.write(line)
if __name__ == '__main__':
    t1 = threading.Thread(target=split_txt)
    t2 = threading.Thread(target=handle_txt)
    t1.start()
    t1.join()
    t2.start()
