# !/usr/bin/env python3
#coding=utf-8
'''
@File   :get_data.py
@Author :lianfeng
@Date   :2019/8/27下午3:17
@Version:1.0
@Desc   : 获取请求url和json文件内容
'''
import codecs
import configparser
import json
import random
import string
import time
import yaml
import os
from testfiles.config_file import params_config


config = configparser.ConfigParser()
proDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 运行环境：0.dev分支 1.昊天  2.本地
run_env = 2


class GetData():

    # 获取请求url
    def get_apm_url(self, inf):
        configPath = proDir + '/testfiles/config_file/config.ini'
        path = os.path.abspath(configPath)
        config.read(path, encoding="utf-8")
        inf_port = ''
        url = ''
        if run_env == 2:
            url = config.get('testServer', 'apm_url')
            inf_port = params_config.port[inf]
        elif run_env == 0:
            url = config.get('devServer', 'apm_url')
            inf_port = params_config.dev_port[inf]
        elif run_env == 1:
            url = config.get('haotianServer', 'apm_url')
            inf_port = params_config.haotian_port[inf]
        url = url + ":" + inf_port
        return url

    # 获取请求token
    def get_cookie(self):
        configPath = proDir + '/testfiles/config_file/config.ini'
        path = os.path.abspath(configPath)
        config.read(path, encoding="utf-8")
        cookie = config.get('apmCookie', 'cookie')
        return {"Cookie": cookie}

    def read_json_file(self,filename):
        """ 读取json文件,返回的是字典
        Args：
            filename: String类型，文件名称；/testfiles/json_data/路径下文件
        return:
            返回json结构数据
        """
        json_fi = codecs.open(proDir+'/testfiles/json_data/'+filename,'r',encoding='utf-8')#
        json_content = json_fi.read()
        json_fi.close()
        return json.loads(json_content.encode('utf-8'))

    def read_yaml_file(self,filename):
        """ 读取yaml文件
        Args：
            filename: String类型，文件名称；/testfiles/json_data/路径下文件
        return:
            返回json结构数据
        """
        yaml_fi = codecs.open(proDir+'/testfiles/json_data/'+filename,'r',encoding='utf-8')
        yaml_content = yaml_fi.read()
        yaml_fi.close()
        return yaml.load(yaml_content.encode('utf-8'),yaml.FullLoader)

    def read_schema_file(self,filename):
        """ 读取schema文件,返回的是字典
        Args：
            filename：String类型，文件名称；/testfiles/schema_file/路径下文件。
        return:
            返回json结构数据
        """
        json_fi = codecs.open(proDir+'/testfiles/schema_file/'+filename,'r',encoding='UTF-8')
        json_content = json_fi.read()
        json_fi.close()
        return json.loads(json_content.encode('UTF-8'))

    #上传数据用，支持单文件和多文件
    def get_filePath(self,filename):
        if type(filename) is str:#判断传参是否为字符串
            # 获取当前脚本所在路径的上层路径，并拼接"test_file"
            file = open(proDir + '/testfiles/upload_file/' + filename, "rb")
            return {"file": file}
        if type(filename) is list:#判断传参是否为列表
            multiple_files = []
            for num in range(0,len(filename)):
                files=('file',open(proDir + '/testfiles/upload_file/' + filename[num], "rb"))
                multiple_files.append(files)
            return multiple_files
