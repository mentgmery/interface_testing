# !/usr/bin/env python3
#coding=utf-8
'''
@File   :setCookie.py
@Author :lianfeng
@Date   :2020/1/15 11:46 PM
@Version:1.0
@Desc   : 获取Cookie，写入config.ini
'''
import configparser
import os
import requests

login_url = "http://192.168.1.244:8881/api/user/login"
login_json = {
    "name": "peri",
    "password": "123456"
}


class Set_Cookie():

    def set_cookie_config(self):
        json_data = requests.post(login_url, login_json, allow_redirects=False) #发送post请求
        Cookie = json_data.headers['Set-Cookie'].split(';')[0]
        #把Cookie写入config.ini文件
        config = configparser.ConfigParser()
        proDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        configPath = proDir + '/testfiles/config_file/config.ini'
        path = os.path.abspath(configPath)
        config.read(path, encoding="utf-8")
        config.set("apmCookie", "Cookie",Cookie)
        config.write(open(path, "w", encoding="utf-8"))