# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_receiver.py
@Author :lianfeng
@Date   :2020/1/21 9:04 AM
@Version:1.0
@Desc   :  数据清洗接收器
'''
import json

from apm_modules.data_cleaning_output import DataCleaningOutput
from apm_modules.data_source_output import DataSourceOutput
from apm_modules.template_mgt_output import TemplateMgtOutput
from common.openbrowser import OpenURL

dc_url = 'http://192.168.1.78:8018/dataetl'#数据清洗—列表URL

class DataCleaningReceiver(OpenURL):

    def datacleaning_receiver_url(self,url,requiredDom):
        """
        数据清洗—接收器，访问url获取元素值
        :param url: 接收器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                数据文件列表：'__data_source_list'
                数据文件详情：'__data_source_detail'
                模板列表：'__data_template-list'
                模板详情：'__data_template-detail'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        value = self.driver.find_element_by_id(requiredDom).is_enabled() # 取什么值自己定位元素
        return value


    def get_dataclean_receiver_datalist_url(self,data):
        """获取接收器—模板列表url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/data_source?params=xxx
        """

        if data is None:
            url = dc_url + '?ENV_OUTPUT_DATA_LIST={}'
            return url
        else:
            url = dc_url + '?ENV_OUTPUT_DATA_LIST=' + json.dumps(data)
            return url


    def get_dataclean_receiver_datadetails_url(self,data):
        """获取接收器—模板详情url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/data_source?params=xxx
        """
        #dc_url = DataCleaningOutput().get_data_cleaning_details_jsonschema().url #数据清洗—详情URL
        if data is None:
            url = dc_url + '?ENV_OUTPUT_DATA_DETAIL={}'
            return url
        else:
            url = dc_url + '?ENV_OUTPUT_DATA_DETAIL=' + json.dumps(data)
            return url

    def get_template_list_url(self,data):
        """获取接收器—数据文件列表url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/template?params=xxx
        """
        #dso_url = DataSourceOutput().datasource_list_validity().url
        if data is None:
            url = dc_url + '?ENV_OUTPUT_TEMPLATE_LIST={}'
            return url
        else:
            url = dc_url + '?ENV_OUTPUT_TEMPLATE_LIST=' + json.dumps(data)
            return url


    def get_template_details_url(self,data):
        """获取接收器—数据文件详情url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/template?params=xxx
        """
        #dso_url = DataSourceOutput().datasource_details_validity().url
        if data is None:
            url = dc_url + '?ENV_OUTPUT_TEMPLATE_DETAIL={}'
            return url
        else:
            url = dc_url + '?ENV_OUTPUT_TEMPLATE_DETAIL=' + json.dumps(data)
            return url
