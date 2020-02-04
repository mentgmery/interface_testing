# !/usr/bin/env python3
#coding=utf-8
'''
@File   :params_config.py
@Author :zhumeng
@Date   :2020/2/3  16:03
@Version:1.0
@Desc   : 参数配置
'''

import json
from common.base_page import BasePage


# 所有api url
dc_output_list_url = "/api/dataset"
dc_output_details_url = "/lensData/lensData/getResultSet"
dc_output_list_headers = None
dc_output_details_headers = None
# 数据源
ds_output_list_url = "/api/data_source"
ds_output_details_url = "/lensData/lensData/getRawData"
ds_output_list_headers = None
ds_output_details_headers = None


# 数据源列表参数
ds_output_list_validity_params ={
            "q_type" : 0,
            "page_size" : 10,
            "page" : 1,
            "case_id" : '598756534'
                    }

ds_output_list_invalid_params = {
            "q_type" : -1,
            "page_size" : 10,
            "page" : 1,
            "case_id" : '598756534'
                    }

ds_output_list_null_q_type = {
    "q_type": None,
    "page_size": 10,
    "page": 1,
    "case_id": '598756534'
}

ds_output_list_invalid_page_size = {
    "q_type": 0,
    "page_size": -1,
    "page": 1,
    "case_id": '598756534'
}

ds_output_list_null_page_size = {
    "q_type": 0,
    "page_size": None,
    "page": 1,
    "case_id": '598756534'
}

ds_output_list_invalid_page = {
    "q_type": 0,
    "page_size": 10,
    "page": -1,
    "case_id": '598756534'
}

ds_output_list_null_page = {
    "q_type": 0,
    "page_size": 10,
    "page": None,
    "case_id": '598756534'
}

ds_output_list_invalid_case_id = {
    "q_type": 0,
    "page_size": 10,
    "page": 1,
    "case_id": '2323xx'
}

ds_output_list_null_case_id={
            "q_type" : 0,
            "page_size" : 10,
            "page" : 1,
            "case_id" : ''
                    }

# 数据源详情参数
ds_output_details_validity = {
    "id": '3DA23E9F-F386-4A0D-87B1-25FFCD06A80D',
    "case_id": '442791611'
}

ds_output_details_invalid_data_id = {
    "id": 'xxxjejl1',
    "case_id": '442791611'
}

ds_output_details_null_data_id = {
    "id": '',
    "case_id": '442791611'
}

ds_output_details_invalid_case_id = {
    "id": '3DA23E9F-F386-4A0D-87B1-25FFCD06A80D',
    "case_id": 'j4irieoro'
}

ds_output_details_null_case_id = {
    "id": '3DA23E9F-F386-4A0D-87B1-25FFCD06A80D',
    "case_id": ''
}

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