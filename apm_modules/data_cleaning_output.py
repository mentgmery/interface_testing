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
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_invalid_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": 111111
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_none_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": None
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_no_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_valid_page_num(self):
        params_dict = {
            "page_size": 20,
            "page": 2,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_size_less_than_page_size(self):
        params_dict = {
            "page_size": 7,
            "page": 1,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_size_more_than_page_size(self):
        params_dict = {
            "page_size": 11,
            "page": 1,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_invalid_page_num(self):
        params_dict = {
            "page_size": 100,
            "page": -1,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_without_page_num(self):
        params_dict = {
            "page_size": 100,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_invalid_page_size(self):
        params_dict = {
            "page_size": -1,
            "page": 0,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_list_by_none_page_size(self):
        params_dict = {
            "page_size": None,
            "page": 0,
            "case_id": 659939916
        }
        return self.get_http_response(list_url, params_dict, headers)

    def get_data_cleaning_details_jsonschema(self):
        params_dict = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": "442791611"
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_invalid_caseid(self):
        params_dict = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": "111111"
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_without_no_caseid(self):
        params_dict = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow"
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_none_caseid(self):
        params_dict = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": ""
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_invalid_data_id(self):
        params_dict = {
            "id": "111111",
            "case_id": "442791611"
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_without_data_id(self):
        params_dict = {
            "case_id": "442791611"
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_none_data_id(self):
        params_dict = {
            "id": "",
            "case_id": "442791611"
        }
        return self.get_http_response(details_url, params_dict, headers)

    def get_data_cleaning_details_by_invalid_params(self):
        params_dict = {
            "xxx": "11111",
            "yyy": "111111"
        }
        return self.get_http_response(details_url, params_dict, headers)