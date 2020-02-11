# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_trigger.py
@Author :lianfeng
@Date   :2020/1/20 10:54 PM
@Version:1.0
@Desc   : 数据清洗—新增数据—触发器
'''
import json
import time

from apm_modules.data_cleaning_ops import DataCleaningOps
from apm_modules.data_source_ops import DataSourceOps
from common.openbrowser import OpenURL

add_data = "//*[@class='data-etl']/section[2]/aside/div[1]/div/button"
clean_close = "//*[@id='__layout']/div/div[2]/div/div/section[2]/div[2]/div/div/div[3]/div/button[2]/span"

class DataCleaningTrigger(OpenURL):

    def get_datacleaning_trigger_jumpetl_id(self,url,requiredDom):
        """
        数据源—触发器，打开浏览器，访问url获取元素值
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                新增数据：'__data_source_jumpetl'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_xpath(clean_close).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(add_data).click()
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        time.sleep(1)
        value = self.driver.find_element_by_id(requiredDom).is_enabled()  # 取什么值自己定位元素
        return value

    def get_datacleaning_trigger_pagesource(self,url):
        """
        数据源—触发器，打开浏览器，访问url获取元素值
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                新增数据：'__data_source_jumpetl'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element_by_xpath(clean_close).click()
        time.sleep(1)
        ps = self.driver.page_source
        return ps

    def get_datacleaning_trigger_add_data_url(self,data):
        """
        获取数据清洗触发器—url
        Returns: 返回get的url 示例：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&ENV_ACTION_ADD=xxxx
        """
        clean_url = DataCleaningOps(self.driver).get_clean_url()  # 获取数据清洗动作—清洗url
        if data is None:
            url = clean_url + '&ENV_ACTION_ADD={}'
            return url
        else:
            url = clean_url + '&ENV_ACTION_ADD=' + json.dumps(data)
            return url
