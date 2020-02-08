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
from common.base_page import BasePage
from testfiles.config_file import params_config


inf_type = 'dc'


class DataSourceOutput(BasePage):

    def datasource_list_validity(self):
        """
            正向的模板管理—列表—输出,请求值均正常。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_validity_params
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_invalid_q_type(self):
        """
            无效的数据源—列表—输出,错误的q_type。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_invalid_params
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_null_q_type(self):
        """
            无效的数据源—列表—输出,q_type为空。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_null_q_type
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_invalid_page_size(self):
        """
            无效的数据源—列表—输出,错误的page_size。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_invalid_page_size
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_null_page_size(self):
        """
            无效的数据源—列表—输出,page_size为空。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_null_page_size
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_invalid_page(self):
        """
            无效的数据源—列表—输出,错误的page。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_invalid_page
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_null_page(self):
        """
            无效的数据源—列表—输出,空的page。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_null_page
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_invalid_case_id(self):
        """
            无效的数据源—列表—输出,错误的case_id
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_invalid_case_id
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_list_null_case_id(self):
        """
            无效的数据源—列表—输出,空的case_id
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_list_null_case_id
        return self.get_http_response(inf_type, params_config.ds_output_list_url, params_dict,
                                      params_config.ds_output_list_headers)

    def datasource_details_validity(self):
        """
            正向的模板管理—详情—输出,请求值均正常。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_details_validity
        return self.get_http_response(inf_type, params_config.ds_output_details_url, params_dict,
                                      params_config.ds_output_details_headers)

    def datasource_details_invalid_data_id(self):
        """
            无效的数据源—详情—输出,错误的data_id。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_details_invalid_data_id
        return self.get_http_response(inf_type, params_config.ds_output_details_url, params_dict,
                                      params_config.ds_output_details_headers)

    def datasource_details_null_data_id(self):
        """
            无效的数据源—详情—输出,data_id为空。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_details_null_data_id
        return self.get_http_response(inf_type, params_config.ds_output_details_url, params_dict,
                                      params_config.ds_output_details_headers)

    def datasource_details_invalid_case_id(self):
        """
            无效的数据源—详情—输出,错误的case_id。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_details_invalid_case_id
        return self.get_http_response(inf_type, params_config.ds_output_details_url, params_dict,
                                      params_config.ds_output_details_headers)

    def datasource_details_null_case_id(self):
        """
            无效的数据源—详情—输出,case_id为空。
            Returns: get请求的结果
        """
        params_dict = params_config.ds_output_details_null_case_id
        return self.get_http_response(inf_type, params_config.ds_output_details_url, params_dict,
                                      params_config.ds_output_details_headers)