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
from testfiles.config_file import params_config
from common.base_page import BasePage
cf = configHTTP.ConfigHttp()

class TemplateMgtOutput(BasePage):

    def templateMgt_list_validity(self):
        """
        正向的模板管理—列表—输出,请求值均正常。
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_validity
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)

    def templateMgt_list_invalid_caseid(self):
        """
        无效的模板管理—列表—输出,错误的case_id
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_invalid_caseid
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)

    def templateMgt_list_null_caseid(self):
        """
        无效的模板管理—列表—输出,空的case_id
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_null_caseid
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)

    def templateMgt_list_invalid_page(self):
        """
        无效的模板管理—列表—输出,page无效的情况
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_invalid_page
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)


    def templateMgt_list_null_page(self):
        """
        无效的模板管理—列表—输出,page为空
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_null_page
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)

    def templateMgt_list_invalid_pagesize(self):
        """
        无效的模板管理—列表—输出,pagesize无效的情况
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_invalid_pagesize
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)

    def templateMgt_list_null_pagesize(self):
        """
        无效的模板管理—列表—输出,pagesize为空
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_list_null_pagesize
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_list_headers)

    def templateMgt_details_validity(self):
        """
        正向的模板管理—详情—输出,请求值均正常。
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_details_validity
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_details_headers)

    def templateMgt_details_invalid_temid(self):
        """
        无效的模板管理—详情—输出,错误的temid
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_details_invalid_temid
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_details_headers)

    def templateMgt_details_null_temid(self):
        """
        无效的模板管理—详情—输出,空的temid
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_details_null_temid
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_details_headers)

    def templateMgt_details_invalid_caseid(self):
        """
        无效的模板管理—详情—输出,错误的caseid
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_details_invalid_caseid
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_details_headers)

    def templateMgt_details_null_caseid(self):
        """
        无效的模板管理—详情—输出,空的caseid
        Returns: get请求的结果
        """
        params_dict = params_config.tm_output_details_null_caseid
        return self.get_http_response(params_config.tm_output_url, params_dict, params_config.tm_output_details_headers)