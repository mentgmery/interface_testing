# !/usr/bin/env python3
#coding=utf-8
'''
@File   :params_config.py
@Author :zhumeng
@Date   :2020/2/3  16:03
@Version:1.0
@Desc   : 参数配置
'''
# 所有api url
dc_output_list_url = "/api/dataset"
dc_output_details_url = "/api/lensData/lensData/getResultSet"
dc_output_list_headers = None
dc_output_details_headers = None
# 数据源
ds_output_list_url = "/api/data_source"
ds_output_details_url = "/lensData/lensData/getRawData"
ds_output_list_headers = None
ds_output_details_headers = None
# 模板管理
tm_output_url = "/api/template"
tm_output_list_headers = None
tm_output_details_headers = None

# 数据源—动作
ds_ops_url = "/filemanagement"
ds_ops_headers = None

# 数据清洗-动作
clean_ops_url = "/dataetl" #清洗
skip_clean_ops_url = "/dataetl"#跳过清洗
clean_ops_headers = None
skip_clean_ops_headers = None

# 数据输出列表测试数据case_id
dc_output_case_id = 817845123
dc_output_id = '02E58ABA-91EA-4A35-9467-38230B772E96-preshow'
data_sid = "7E06FACE-0921-472F-BF52-C070750544D4"

# 数据源测试数据case_id
ds_output_case_id = 817845123


# 数据清洗-动作-参数
clean_data = {
    "case_id": "817845123",
    "sDid": data_sid
}

skip_clean_data = {
    "case_id": "817845123",
    "sDid": data_sid,
    "is_jump": 'true'
}

# 数据源-动作-新增数据参数(这里参数有问题，问开发)
ds_ops_add_data = {
    "openfile":"true",
    "orign_url":"http://192.168.1.78:8018"
}

# 模板管理-列表参数
tm_output_list_validity={
                    "page_size" : 100,
                    "page" : 1,
                    "case_id" : '442791611'
                    }

tm_output_list_invalid_caseid = {
    "page_size": 100,
    "page": 1,
    "case_id": 'cuowu12'
}

tm_output_list_null_caseid = {
    "page_size": 100,
    "page": 1,
    "case_id": ''
}

tm_output_list_invalid_page = {
    "page_size": 100,
    "page": 0,
    "case_id": dc_output_case_id
}

tm_output_list_null_page = {
    "page_size": 100,
    "page": None,
    "case_id": dc_output_case_id
}

tm_output_list_invalid_pagesize = {
    "page_size": -1,
    "page": 1,
    "case_id": dc_output_case_id
}

tm_output_list_null_pagesize = {
    "page_size": None,
    "page": 1,
    "case_id": dc_output_case_id
}
# 模板管理—详情参数
tm_output_details_validity = {
    "tem_id": '777777',
    "case_id": dc_output_case_id
}

tm_output_details_invalid_temid = {
    "tem_id": '我是错误的',
    "case_id": dc_output_case_id
}

tm_output_details_null_temid = {
    "tem_id": "",
    "case_id": dc_output_case_id
}

tm_output_details_invalid_caseid = {
    "tem_id": '777777',
    "case_id": '23563'  # 错误的值
}

tm_output_details_null_caseid = {
    "tem_id": '777777',
    "case_id": ''  # 空的值
}

# 数据源清洗列表参数
dc_output_list_schema_check_params = {
            "page_size": 100,
            "page": 1,
            "case_id": dc_output_case_id
        }

dc_output_list_valid_caseid_params = {
            "page_size": 100,
            "page": 1,
            "case_id": dc_output_case_id
        }

dc_output_list_invalid_caseid_params = {
            "page_size": 100,
            "page": 1,
            "case_id": 111111
        }

dc_output_list_none_caseid_params = {
            "page_size": 100,
            "page": 1,
            "case_id": None
        }

dc_output_list_without_caseid_params = {
            "page_size": 100,
            "page": 1
        }

dc_output_list_by_valid_page_num = {
            "page_size": 10,
            "page": 1,
            "case_id": dc_output_case_id
        }
dc_output_list_by_invalid_page_num = {
            "page_size": 100,
            "page": -1,
            "case_id": dc_output_case_id
        }

dc_output_list_without_page_num = {
            "page_size": 100,
            "case_id": dc_output_case_id
        }

dc_output_list_invalid_page_size = {
            "page_size": -1,
            "page": 0,
            "case_id": dc_output_case_id
        }

dc_output_list_less_than_page_size = {
            "page_size": 14,
            "page": 1,
            "case_id": dc_output_case_id
        }

dc_output_list_more_than_page_size = {
            "page_size": 7,
            "page": 1,
            "case_id": dc_output_case_id
        }

dc_output_list_none_page_size = {
            "page_size": None,
            "page": 0,
            "case_id": dc_output_case_id
        }

dc_output_list_without_page_size = {
            "page": 0,
            "case_id": dc_output_case_id
        }


# 数据源清洗详情参数
dc_output_details_schema_check_params = {
            "id": dc_output_id,
            "case_id": dc_output_case_id
        }

dc_output_details_invalid_caseid_params = {
            "id": dc_output_id,
            "case_id": "111111"
        }

dc_output_details_without_caseid_params = {
            "id": dc_output_id
        }

dc_output_details_none_caseid_params = {
            "id": dc_output_id,
            "case_id": ""
        }

dc_output_details_invalid_dataid_params = {
            "id": "111111",
            "case_id": dc_output_case_id
        }

dc_output_details_without_dataid_params = {
            "case_id": dc_output_case_id
        }

dc_output_details_by_none_dataid_params = {
            "id": "",
            "case_id": dc_output_case_id
        }

dc_output_details_by_invalid_params = {
            "xxx": "11111",
            "yyy": "111111"
        }

# 数据源列表参数
ds_output_list_validity_params ={
            "q_type" : 0,
            "page_size" : 10,
            "page" : 1,
            "case_id" : ds_output_case_id
                    }

ds_output_list_invalid_params = {
            "q_type" : -1,
            "page_size" : 10,
            "page" : 1,
            "case_id" : ds_output_case_id
                    }

ds_output_list_null_q_type = {
    "q_type": None,
    "page_size": 10,
    "page": 1,
    "case_id": ds_output_case_id
}

ds_output_list_invalid_page_size = {
    "q_type": 0,
    "page_size": -1,
    "page": 1,
    "case_id": ds_output_case_id
}

ds_output_list_null_page_size = {
    "q_type": 0,
    "page_size": None,
    "page": 1,
    "case_id": ds_output_case_id
}

ds_output_list_invalid_page = {
    "q_type": 0,
    "page_size": 10,
    "page": -1,
    "case_id": ds_output_case_id
}

ds_output_list_null_page = {
    "q_type": 0,
    "page_size": 10,
    "page": None,
    "case_id": ds_output_case_id
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
    "case_id": ds_output_case_id，
    "id": data_sid
}

ds_output_details_invalid_data_id = {
    "id": 'xxxjejl1',
    "case_id": ds_output_case_id
}

ds_output_details_null_data_id = {
    "id": '',
    "case_id": ds_output_case_id
}

ds_output_details_invalid_case_id = {
    "id": data_sid,
    "case_id": 'j4irieoro'
}

ds_output_details_null_case_id = {
    "id": data_sid,
    "case_id": ''
}