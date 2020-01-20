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
dco_url = "/api/dataset"


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
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_invalid_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": 111111
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_none_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1,
            "case_id": None
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_no_caseid(self):
        params_dict = {
            "page_size": 100,
            "page": 1
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_valid_page_num(self):
        params_dict = {
            "page_size": 20,
            "page": 2,
            "case_id": 659939916
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_invalid_page_num(self):
        params_dict = {
            "page_size": 100,
            "page": -1,
            "case_id": 659939916
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_invalid_page_size(self):
        params_dict = {
            "page_size": -1,
            "page": 0,
            "case_id": 659939916
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()

    def get_data_cleaning_list_by_none_page_size(self):
        params_dict = {
            "page_size": None,
            "page": 0,
            "case_id": 659939916
        }
        cf.set_url(dco_url)
        cf.set_params(params_dict)
        cf.set_headers(None)
        return cf.get()
