# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_source_ops.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 数据源动作
'''
import json,time
from common import configHTTP
from common.openbrowser import OpenURL

cf = configHTTP.ConfigHttp()

ops_url = "/filemanagement"

class DataSourceOps(OpenURL):

    def get_datasource_add_data_url(self):
        """获取新增数据url
        :return: 返回请求的url 示例: http://192.168.1.244:8881/filemanagement?case_id=xxxx
        """
        dict_data = {
            "case_id" : "442791611"
        }
        cf.set_url(ops_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get().url

    def datasource_add_data(self,url):
        """
        数据源—动作，打开浏览器，访问url获取元素值
        :param url: 动作的url地址
        :return: 特定元素的属性值。
        """
        self.driver.get(url)
        #self.driver.page_source
        #id_value=self.driver.find_element_by_id('su').get_attribute("value")#取什么值自己定位元素
        visible=self.driver.find_element_by_id('su').is_displayed()# 判断元素是否存在
        return visible