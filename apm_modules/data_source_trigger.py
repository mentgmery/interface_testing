# !/usr/bin/env python3
#coding=utf-8
'''
@File   : data_source_trigger.py
@Author : lianfeng
@Date   : 2020/1/19 5:16 PM
@Version: 1.0
@Desc   : 数据源—清洗/跳过清洗—触发器
'''
import json

from apm_modules.data_cleaning_ops import DataCleaningOps
from common import configHTTP
from common.openbrowser import OpenURL

cf = configHTTP.ConfigHttp()

#dataSource_url = "xxxxx"
dataSource_url = "/api/template"

class DataSourceTrigger(OpenURL):

    def datasource_trigger_url(self,url,requiredDom):
        """
        数据源—触发器，打开浏览器，访问url获取元素值
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                清洗：'__data_source_etl'，
                跳过清洗：'__data_source_jumpetl'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        #self.driver.page_source
        value = self.driver.find_element_by_id(requiredDom).is_displayed() # 取什么值自己定位元素
        #visible = self.driver.find_element_by_id('su').is_displayed() # 取什么值自己定位元素
        return value

    def get_datasource_trigger_clean_url(self,data):
        """
        获取数据源触发器—清洗—url
        Returns: 返回get的url 示例：
                非空：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&ENV_ACTION_CLEAN=xxxx
                空：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&ENV_ACTION_CLEAN={}
        """
        clean_url=DataCleaningOps(self.driver).get_clean_url() # 获取数据清洗动作—清洗url
        if data is None:
            url = clean_url + '&ENV_ACTION_CLEAN={}'
            return url
        else:
            url = clean_url + '&ENV_ACTION_CLEAN=' + str(data)
            return url

    def get_datasource_trigger_skip_clean_url(self,data):
        """
        获取数据源触发器—跳过清洗—url
        Returns: 返回get的url 示例：
                非空：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&ENV_ACTION_SKIP_CLEAN=xxxx
                空：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&ENV_ACTION_SKIP_CLEAN={}
        """
        skip_clean_url=DataCleaningOps(self.driver).get_skip_clean_url() # 获取数据清洗动作—跳过清洗url
        if data is None:
            url = skip_clean_url + '&ENV_ACTION_SKIP_CLEAN={}'
            return url
        else:
            url = skip_clean_url + '&ENV_ACTION_SKIP_CLEAN=' + str(skip_clean_data)
            return url