# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_ops.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 数据清洗动作
'''

import json
from common import configHTTP
from common.getData import GetData
from common.openbrowser import OpenURL

cf = configHTTP.ConfigHttp()

clean_url = "/dataetl"

skip_clean_url = "/filemanagement"

class DataCleaningOps(OpenURL):

    def get_clean_url(self):
        """获取清洗url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx
        """
        dict_data = {
          "case_id": "908651985",
          "sDid" : "B338F6FE-8F93-4037-A99A-D36EE67CA1E6"
        }
        cf.set_url(clean_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get().url

    def get_skip_clean_url(self):
        """获取清洗url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/filemanagement?case_id=xxxx&sDid=xxxx
        """
        dict_data = {
          "case_id": "908651985",
          "sDid" : "B338F6FE-8F93-4037-A99A-D36EE67CA1E6"
        }
        cf.set_url(skip_clean_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get().url

    def data_cleaning_ops(self,url):
        """
        数据源—动作，打开浏览器，访问url获取元素值
        :param url: 动作的url地址 清洗/跳过清洗
        :return: 特定元素的属性值。
        """
        self.driver.get(url)
        #self.driver.page_source
        #id_value=self.driver.find_element_by_id('su').get_attribute("value")#取什么值自己定位元素
        visible=self.driver.find_element_by_id('su').is_displayed()# 判断元素是否存在
        return visible
