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
import time


from common import configHTTP
from common.base_page import BasePage
from common.openbrowser import OpenURL
from apm_modules.data_source_output import DataSourceOutput as dso
cf = configHTTP.ConfigHttp()

clean = "//*[@class='el-table__fixed-right']/div[2]/table/tbody/tr[1]/td[5]/div/button[2]/span"
skip_clean = "//*[@class='el-table__fixed-right']/div[2]/table/tbody/tr[1]/td[5]/div/button[3]/span"
inf_type = 'ds'
dst_data_url = dso().get_datasource_trigger_url()


class DataSourceTrigger(OpenURL,BasePage):

    def get_datasource_trigger_etl_id(self,url,requiredDom):
        """
        数据源—触发器-清洗，打开浏览器，访问url—dom树种是否包含__data_source_etl
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                清洗：'__data_source_etl'，
                跳过清洗：'__data_source_jumpetl'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_xpath(clean).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        time.sleep(1)
        value = self.driver.find_element_by_id(requiredDom).is_enabled() # 取什么值自己定位元素
        return value



    def get_datasource_trigger_jumpetl_id(self,url,requiredDom):
        """
        数据源—触发器—跳过清洗，打开浏览器，访问url—dom树种是否包含__data_source_jumpetl
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                清洗：'__data_source_etl'，
                跳过清洗：'__data_source_jumpetl'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_xpath(skip_clean).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        time.sleep(1)
        value = self.driver.find_element_by_id(requiredDom).is_enabled() # 取什么值自己定位元素
        return value

    def get_datasource_trigger_list_value(self,url):
        """
        数据源—列表中—右侧操作列—value值
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                清洗：'__data_source_etl'，
                跳过清洗：'__data_source_jumpetl'
        :return: 元素的值
        """
        self.driver.get(url)
        text=self.driver.find_element_by_xpath(clean).text
        return text


    def get_datasource_trigger_clean_url(self,data):
        """
        获取数据源触发器—清洗—url
        Returns: 返回get的url 示例：
                非空：http://192.168.1.78:8016/filemanagement?case_id=xxxx&sDid=xxxx&ENV_ACTION_CLEAN=xxxx
                空：http://192.168.1.78:8016/filemanagement?case_id=xxxx&sDid=xxxx&ENV_ACTION_CLEAN={}
        """
        #clean_url=DataCleaningOps(self.driver).get_clean_url() # 获取数据清洗动作—清洗url
        if data is None:
            url = dst_data_url + '&ENV_ACTION_CLEAN={}'
            return url
        else:
            url = dst_data_url + '&ENV_ACTION_CLEAN=' + json.dumps(data)
            return url

    def get_datasource_trigger_skip_clean_url(self,data):
        """
        获取数据源触发器—跳过清洗—url
        Returns: 返回get的url 示例：
                非空：http://192.168.1.78:8016/filemanagement?case_id=xxxx&sDid=xxxx&ENV_ACTION_SKIP_CLEAN=xxxx
                空：http://192.168.1.78:8016/filemanagement?case_id=xxxx&sDid=xxxx&ENV_ACTION_SKIP_CLEAN={}
        """
        if data is None:
            url = dst_data_url + '&ENV_ACTION_SKIP_CLEAN={}'
            return url
        else:
            url = dst_data_url + '&ENV_ACTION_SKIP_CLEAN=' + json.dumps(data)
            return url
