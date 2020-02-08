# !/usr/bin/env python3
#coding=utf-8
'''
@File   :base_page.py
@Author :zhumeng
@Date   :2020/1/23  下午3:13
@Version:1.0
@Desc   : 重构基础方法类
'''
import json
import requests
from common.configHTTP import ConfigHttp


cf = ConfigHttp()


class BasePage:

    def get_http_response(self, inf_type, api_path, params, headers):
        '''
        根据用户提供的项目名、端口号去判断项目的url拼接
        :param api_path:
        :return:
        '''
        cf.set_url(api_path, inf_type)
        cf.set_params(params)
        cf.set_headers(headers)
        return cf.get()
