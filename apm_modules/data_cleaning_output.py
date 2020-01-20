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
from common import configHTTP
from common.getData import GetData

cf = configHTTP.ConfigHttp()
list_url = "/api/dataset"
details_url = "/lensData/lensData/getResultSet"


class DataCleaningOutput():

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
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_invalid_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": 111111
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_none_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": None
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_no_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_valid_page_num(self):
        params_dict = {
            "page_size": 20,
            "page": 2,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_size_less_than_page_size(self):
        params_dict = {
            "page_size": 7,
            "page": 1,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_size_more_than_page_size(self):
        params_dict = {
            "page_size": 11,
            "page": 1,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_invalid_page_num(self):
        params_dict = {
            "page_size": 100,
            "page": -1,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_without_page_num(self):
        params_dict = {
            "page_size": 100,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_invalid_page_size(self):
        params_dict = {
            "page_size": -1,
            "page": 0,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_none_page_size(self):
        params_dict = {
            "page_size": None,
            "page": 0,
            "case_id": 659939916
        }
        cf.set_url(list_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_jsonschema(self):
        params_dict = {
            "data_id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": "442791611"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_by_invalid_caseid(self):
        params_dict = {
            "data_id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": "111111"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_without_no_caseid(self):
        params_dict = {
            "data_id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_by_none_caseid(self):
        params_dict = {
            "data_id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": ""
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_by_invalid_data_id(self):
        params_dict = {
            "data_id": "111111",
            "case_id": "442791611"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_without_data_id(self):
        params_dict = {
            "case_id": "442791611"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_by_none_data_id(self):
        params_dict = {
            "data_id": "",
            "case_id": "442791611"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_details_by_invalid_params(self):
        params_dict = {
            "id": "11111",
            "value": "111111"
        }
        cf.set_url(details_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()