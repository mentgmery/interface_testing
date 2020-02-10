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
from common.base_page import BasePage

from common.openbrowser import OpenURL
from testfiles.config_file import params_config

cf = configHTTP.ConfigHttp()

inf_type = 'dc'

class DataCleaningOps(OpenURL,BasePage):

    def get_clean_url(self):
        """获取清洗url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx
        """
        params_dict = params_config.clean_data
        return self.get_http_response(inf_type,params_config.clean_ops_url, params_dict, params_config.clean_ops_headers).url

    def get_skip_clean_url(self):
        """获取清洗url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&is_jump=true
        """
        params_dict = params_config.skip_clean_data
        return self.get_http_response(inf_type,params_config.skip_clean_ops_url, params_dict, params_config.skip_clean_ops_headers).url

    def data_cleaning_ops(self,url,requiredDom):
        """
        数据源—动作，打开浏览器，访问url获取元素值
        :param url: 动作的url地址 清洗/跳过清洗
        :param requiredDom: Dom树中id值
                清洗：'__data_source_etl'，
                跳过清洗：'__data_source_jumpetl'
        :return: 特定元素的属性值。
        """
        self.driver.get(url)
        print(url)
        #self.driver.page_source
        #id_value=self.driver.find_element_by_id('su').get_attribute("value")#取什么值自己定位元素
        visible=self.driver.find_element_by_id(requiredDom).is_enabled()# 判断元素是否可用
        return visible