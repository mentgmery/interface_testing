# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_source_output.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 数据源输出
'''

import json
from common import configHTTP

cf = configHTTP.ConfigHttp()

data_source_url = "/api/data_source"

class DataSourceOutput():

    def datasource_list_validity(self):
        """
            正向的模板管理—列表—输出,请求值均正常。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : 10,
            "page" : 1,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_invalid_q_type(self):
        """
            无效的数据源—列表—输出,错误的q_type。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : -1,
            "page_size" : 10,
            "page" : 1,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_null_q_type(self):
        """
            无效的数据源—列表—输出,q_type为空。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : None,
            "page_size" : 10,
            "page" : 1,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_invalid_page_size(self):
        """
            无效的数据源—列表—输出,错误的page_size。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : -1,
            "page" : 1,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()


    def datasource_list_null_page_size(self):
        """
            无效的数据源—列表—输出,page_size为空。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : None,
            "page" : 1,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_invalid_page(self):
        """
            无效的数据源—列表—输出,错误的page。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : 10,
            "page" : -1,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_null_page(self):
        """
            无效的数据源—列表—输出,空的page。
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : 10,
            "page" : None,
            "case_id" : '598756534'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_invalid_case_id(self):
        """
            无效的数据源—列表—输出,错误的case_id
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : 10,
            "page" : 1,
            "case_id" : '2323xx'
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_list_null_case_id(self):
        """
            无效的数据源—列表—输出,空的case_id
            Returns: get请求的结果
        """
        dict_data = {
            "q_type" : 0,
            "page_size" : 10,
            "page" : 1,
            "case_id" : ''
                    }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_details_validity(self):
        """
            正向的模板管理—详情—输出,请求值均正常。
            Returns: get请求的结果
        """
        dict_data =  {
                "data_id" : '3DA23E9F-F386-4A0D-87B1-25FFCD06A80D',
                "case_id" : '442791611'
                }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()


    def datasource_details_invalid_data_id(self):
        """
            无效的数据源—详情—输出,错误的data_id。
            Returns: get请求的结果
        """
        dict_data =  {
                "data_id" : 'xxxjejl1',
                "case_id" : '442791611'
                }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_details_null_data_id(self):
        """
            无效的数据源—详情—输出,data_id为空。
            Returns: get请求的结果
        """
        dict_data =  {
                "data_id" :  '',
                "case_id" : '442791611'
                }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_details_invalid_case_id(self):
        """
            无效的数据源—详情—输出,错误的case_id。
            Returns: get请求的结果
        """
        dict_data =  {
                "data_id" : '3DA23E9F-F386-4A0D-87B1-25FFCD06A80D',
                "case_id" : 'j4irieoro'
                }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def datasource_details_null_case_id(self):
        """
            无效的数据源—详情—输出,case_id为空。
            Returns: get请求的结果
        """
        dict_data =  {
                "data_id" : '3DA23E9F-F386-4A0D-87B1-25FFCD06A80D',
                "case_id" : ''
                }
        cf.set_url(data_source_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()