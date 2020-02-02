# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_output.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 数据清洗输出
'''

import json
from common.base_page import BasePage
from common.getData import GetData
from testfiles.config_file import params_config


#cf = configHTTP.ConfigHttp()
list_url = "/api/dataset"
details_url = "/lensData/lensData/getResultSet"
headers = None


class DataCleaningOutput(BasePage):

    '''
    @Author : zhumeng
    @Desc   :
    @param  :
    '''
    def get_data_cleaning_list_jsonschema(self):
        params_dict = params_config.dc_output_list_schema_check_params
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_invalid_caseid(self):
        params_dict = params_config.dc_output_list_invalid_caseid_params
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_none_caseid(self):
        params_dict = params_config.dc_output_list_none_caseid_params
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_no_caseid(self):
        params_dict = params_config.dc_output_list_without_caseid_params
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_valid_page_num(self):
        params_dict = params_config.dc_output_list_by_valid_page_num
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_size_less_than_page_size(self):
        params_dict = params_config.dc_output_list_less_than_page_size
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_size_more_than_page_size(self):
        params_dict = params_config.dc_output_list_more_than_page_size
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_invalid_page_num(self):
        params_dict = params_config.dc_output_list_by_invalid_page_num
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_without_page_num(self):
        params_dict = params_config.dc_output_list_without_page_num
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_invalid_page_size(self):
        params_dict = params_config.dc_output_list_invalid_page_size
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_none_page_size(self):
        params_dict = params_config.dc_output_list_none_page_size
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_details_jsonschema(self):
        params_dict = params_config.dc_output_details_schema_check_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_invalid_caseid(self):
        params_dict = params_config.dc_output_details_invalid_caseid_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_without_no_caseid(self):
        params_dict = params_config.dc_output_details_without_caseid_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_none_caseid(self):
        params_dict = params_config.dc_output_details_none_caseid_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_invalid_data_id(self):
        params_dict = params_config.dc_output_details_invalid_dataid_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_without_data_id(self):
        params_dict = params_config.dc_output_details_without_dataid_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_none_data_id(self):
        params_dict = params_config.dc_output_details_by_none_dataid_params
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_invalid_params(self):
        params_dict = params_config.dc_output_details_by_invalid_params
        return self.get_http_response(details_url, params_dict, headers)