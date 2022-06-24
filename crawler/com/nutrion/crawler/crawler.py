#!/usr/bin/python
# -*- coding: UTF-8 -*-
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
headers = {
    'User-Agent':agent
}

from urllib import request, parse
import urllib
from fake_useragent import UserAgent
# urlopen()向URL发请求,返回响应对象
#response=urllib.request.urlopen('http://www.baidu.com/')
response=urllib.request.urlopen('http://httpbin.org/get')

url = 'http://httpbin.org/get'


# 拼接URL地址
def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    #此处使用urlencode()进行编码
    params = parse.urlencode({'wd':word})
    url = url.format(params)
    return url
# 发请求,保存本地文件
def request_url(url,filename):
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    # 请求对象 + 响应对象 + 提取内容
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件至本地
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)
# 主程序入口
if __name__ == '__main__':
    word = input('请输入搜索内容:')
    url = get_url(word)
    filename = word + '.html'
    print(url)
    request_url(url,filename)

def generate_string():
    # 1、字符串相加
    baseurl = 'http://www.baidu.com/s?'
    params='wd=%E7%88%AC%E8%99%AB'
    url = baseurl + params
    # 2、字符串格式化（占位符）
    params='wd=%E7%88%AC%E8%99%AB'
    url = 'http://www.baidu.com/s?%s'% params
    # 3、format()方法
    url = 'http://www.baidu.com/s?{}'
    params='wd=%E7%88%AC%E8%99%AB'
    url = url.format(params)


def generate_ua():

    ua=UserAgent()
    #随机获取一个ie浏览器ua
    print(ua.ie)
    print(ua.ie)
    #随机获取一个火狐浏览器ua
    print(ua.firefox)
    print(ua.firefox)