#coding：utf8
#author: colatiger
#contact: gxkakuken@gmail.com
#file: gethy.py
#time: 2020-05-01 9:05
import requests
import re

# 需要解析的网址，例：“https://www.huya.com/11352970”
# url=""

#定义函数
def gethy(url):
#获取网页源码
    html=(requests.get(url)).text
#获取标题
    title_regex=(r'<h1 id="J_roomTitle" title="(.*)?"')
    title=re.search(title_regex,html)
    print("频道标题："+title[1])
#获取sStreamName
    sStreamName_regex=(r"sStreamName\":\"([^a-z]*)-A-0-1")
    sStreamName=re.search(sStreamName_regex,html)
    print("真实播放地址：rtmp://aldirect.hls.huya.com/huyalive/"+sStreamName[1]+"-A-0-1")

while (1>0):
    url=input("请输入虎牙播放地址：")
    gethy(url)
    r=input("回车键继续！")