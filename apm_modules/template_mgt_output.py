# !/usr/bin/env python3
#coding=utf-8
'''
@File   :template_mgt_output.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 模板管理—输出
'''

import json
from common import configHTTP
from common.getData import GetData

cf = configHTTP.ConfigHttp()

templateMgt_url = "/api/template"

class TemplateMgtOutput():

    def templateMgt_list_validity(self):
        """
        正向的模板管理—列表—输出,请求值均正常。
        Returns: get请求的结果
        """
        dict_data = {
                    "page_size" : 100,
                    "page" : 1,
                    "case_id" : '442791611'
                    }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_list_invalid_caseid(self):
        """
        无效的模板管理—列表—输出,错误的case_id
        Returns: get请求的结果
        """
        dict_data = {
                    "page_size" : 100,
                    "page" : 1,
                    "case_id" : 'cuowu12'
                    }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_list_null_caseid(self):
        """
        无效的模板管理—列表—输出,空的case_id
        Returns: get请求的结果
        """
        dict_data = {
                    "page_size" : 100,
                    "page" : 1,
                    "case_id" : ''
                    }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_list_invalid_page(self):
        """
        无效的模板管理—列表—输出,page无效的情况
        Returns: get请求的结果
        """
        dict_data = {
            "page_size": 100,
            "page": 0,
            "case_id": '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()


    def templateMgt_list_null_page(self):
        """
        无效的模板管理—列表—输出,page为空
        Returns: get请求的结果
        """
        dict_data = {
            "page_size": 100,
            "page": None,
            "case_id": '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_list_invalid_pagesize(self):
        """
        无效的模板管理—列表—输出,pagesize无效的情况
        Returns: get请求的结果
        """
        dict_data = {
            "page_size": -1,
            "page": 1,
            "case_id": '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_list_null_pagesize(self):
        """
        无效的模板管理—列表—输出,pagesize为空
        Returns: get请求的结果
        """
        dict_data = {
            "page_size": None,
            "page": 1,
            "case_id": '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_details_validity(self):
        """
        正向的模板管理—详情—输出,请求值均正常。
        Returns: get请求的结果
        """
        dict_data = {
            "tem_id" : '777777',
            "case_id" : '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_details_invalid_temid(self):
        """
        无效的模板管理—详情—输出,错误的temid
        Returns: get请求的结果
        """
        dict_data = {
            "tem_id" : '我是错误的',
            "case_id" : '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_details_null_temid(self):
        """
        无效的模板管理—详情—输出,空的temid
        Returns: get请求的结果
        """
        dict_data = {
            "tem_id" : "",
            "case_id" : '442791611'
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_details_invalid_caseid(self):
        """
        无效的模板管理—详情—输出,错误的caseid
        Returns: get请求的结果
        """
        dict_data = {
            "tem_id" : '777777',
            "case_id" : '23563'#错误的值
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()

    def templateMgt_details_null_caseid(self):
        """
        无效的模板管理—详情—输出,空的caseid
        Returns: get请求的结果
        """
        dict_data = {
            "tem_id" : '777777',
            "case_id" : '' #空的值
        }
        cf.set_url(templateMgt_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        return cf.get()