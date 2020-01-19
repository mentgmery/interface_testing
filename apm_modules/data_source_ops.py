# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_source_ops.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 数据源动作
'''

import json
import time

from common import configHTTP
from common.openbrowser import OpenURL

cf = configHTTP.ConfigHttp()


class DataSourceOps(OpenURL):

    def datasource_add_data(self,url):
        """
        数据源—动作，打开浏览器，访问url获取元素值
        :param url: 动作的url地址
        :return: 特定元素的属性值。
        """
        self.driver.get(url)
        #self.driver.page_source
        #id_value=self.driver.find_element_by_id('su').get_attribute("value")#取什么值自己定位元素
        id_value=self.driver.find_element_by_id('su').is_displayed()# 判断元素是否存在
        return id_value