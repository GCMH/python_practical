#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8

from urllib.parse import quote
from urllib import request  # 从urllib包中引入request模块
import urllib.request
import urllib.parse
import string
import json

def getRobotReply_qyk(msg):
    '''
    函数功能：调用青云客API根据内容给出智能回复\n
    返回值  ：返回Str类型的回复内容    
    '''
    try:
        url = r"http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s" % msg;
        url = quote(url, safe=string.printable);#url包含中文需要进行处理
        response = request.urlopen(url)
        content = response.read()#读取响应内容,响应为字节
        dic = json.loads(content.decode("utf-8"))#字节转换为字符,然后json字符串转换为字典
        answer =  dic["content"]
    except Exception as e:
        answer = "进水了,排水中.进水原因%s" % e   
        return answer

def getRobotReply_dj(msg):
    '''
    函数功能：调用itmojun_API根据内容给出智能回复\n
    返回值  ：返回Str类型的回复内容    
    '''
    try:
        #接口参数需要通过urlencode编码，后续还需使用encod转换为字节
        params = urllib.parse.urlencode({"msg":msg}).encode()
        req = urllib.request.Request(r"http://api.itmojun.com/chat_robot",params,method="POST")
        answer = urllib.request.urlopen(req).read().decode("utf-8")
    except Exception as e:
        answer = "进水了,排水中.进水原因%s" % e
    return answer

def main():
    msg = "你好";
    print("青云客聊天API:", getRobotReply_qyk(msg))
    print("itmojun聊天API:", getRobotReply_dj(msg))



main()