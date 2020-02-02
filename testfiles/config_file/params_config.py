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


# 数据源清洗列表参数
dc_output_list_schema_check_params = {
            "page_size": 100,
            "page": 1,
            "case_id": 659939916
        }

dc_output_list_valid_caseid_params = {
            "page_size": 100,
            "page": 1,
            "case_id": 659939916
        }

dc_output_list_invalid_caseid_params = {
            "page_size": 100,
            "page": 1,
            "case_id": 111111
        }

dc_output_list_none_caseid_params = {
            "page_size": 100,
            "page": 1
        }

dc_output_list_without_caseid_params = {
            "page_size": 100,
            "page": 1
        }

dc_output_list_by_valid_page_num = {
            "page_size": 20,
            "page": 2,
            "case_id": 659939916
        }
dc_output_list_by_invalid_page_num = {
            "page_size": 100,
            "page": -1,
            "case_id": 659
        }

dc_output_list_without_page_num = {
            "page_size": 100,
            "case_id": 659939916
        }

dc_output_list_invalid_page_size = {
            "page_size": -1,
            "page": 0,
            "case_id": 659939916
        }

dc_output_list_less_than_page_size = {
            "page_size": 7,
            "page": 1,
            "case_id": 659939
        }

dc_output_list_more_than_page_size = {
            "page_size": 11,
            "page": 1,
            "case_id": 659939916
        }

dc_output_list_none_page_size = {
            "page_size": None,
            "page": 0,
            "case_id": 659939916
        }

dc_output_list_without_page_size = {
            "page": 0,
            "case_id": 659939916
        }


# 数据源清洗详情参数
dc_output_details_schema_check_params = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": "442791611"
        }

dc_output_details_invalid_caseid_params = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": "111111"
        }

dc_output_details_without_caseid_params = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow"
        }

dc_output_details_none_caseid_params = {
            "id": "1B53FC68-A2BE-45E9-A091-1722F2246B3B-preshow",
            "case_id": ""
        }

dc_output_details_invalid_dataid_params = {
            "id": "111111",
            "case_id": "442791611"
        }

dc_output_details_without_dataid_params = {
            "case_id": "442791611"
        }

dc_output_details_by_none_dataid_params = {
            "id": "",
            "case_id": "442791611"
        }

dc_output_details_by_invalid_params = {
            "xxx": "11111",
            "yyy": "111111"
        }

