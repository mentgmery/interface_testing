# !/usr/bin/env python3
#coding=utf-8
'''
@File   :test_data_source.py
@Author :zhumeng
@Date   :2020/1/7下午3:20
@Version:1.0
@Desc   :
'''
import pytest
import allure
from jsonschema import validate
from apm_modules.data_cleaning_output import DataCleaningOutput
from common.getData import GetData


dc = DataCleaningOutput()
data_cleaning_list_schema = GetData().read_schema_file('data_cleaning_list.schema')
data_cleaning_details_schema = GetData().read_schema_file('data_cleaning_details.schema')


@allure.feature("数据清洗—输出")
class TestDataCleaningOutput():

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出-schema校验")
    def test_data_cleaning_output_schema_check(self):
        json_data = dc.get_data_cleaning_list_jsonschema().json()
        validate(json_data, schema=data_cleaning_list_schema)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—有效case_id参数")
    def test_data_cleaning_valid_case_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_jsonschema().json()
        data_value = json_data["data"]["data"]
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—无效case_id参数")
    def test_data_cleaning_invalid_case_id(self):
        """
        验证数据源列表—无效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_by_invalid_caseid().json()
        data_value = json_data["data"]["data"]
        print(data_value)
        assert len(data_value) == 0

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—case_id参数值为空")
    def test_data_cleaning_no_value_case_id(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_by_none_caseid().json()
        data_value = json_data["data"]["data"]
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—无case_id参数")
    def test_data_cleaning_without_case_id(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_by_no_caseid().json()
        data_value = json_data["data"]["data"]
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—有效page参数")
    def test_data_cleaning_with_valid_page_num(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_by_valid_page_num().json()
        data_value = json_data["data"]["data"]
        page_size = json_data["data"]["pageSize"]
        total_pages = json_data["data"]["totalPages"]
        assert page_size == 20
        assert total_pages == 1
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—实际size<page_size参数")
    def test_data_cleaning_with_size_less_than_page_size(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_size_more_than_page_size().json()
        data_value = json_data["data"]["data"]
        count = json_data["data"]["count"]
        page_size = json_data["data"]["pageSize"]
        total_pages = json_data["data"]["totalPages"]
        assert page_size == 7
        assert total_pages == 2
        assert count == 10
        assert len(data_value) == 7

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—实际size>page_size参数")
    def test_data_cleaning_details_with_size_less_than_page_size(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_size_more_than_page_size().json()
        data_value = json_data["data"]["data"]
        count = json_data["data"]["count"]
        page_size = json_data["data"]["pageSize"]
        total_pages = json_data["data"]["totalPages"]
        assert page_size == 11
        assert total_pages == 1
        assert count == 10
        assert len(data_value) == 10

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—无效的page num")
    def test_data_cleaning_details_with_invalid_page_num(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_by_invalid_page_num().json()
        data_value = json_data["data"]["data"]
        count = json_data["data"]["count"]
        page_size = json_data["data"]["pageSize"]
        total_pages = json_data["data"]["totalPages"]
        assert page_size == 100
        assert total_pages == 1
        assert count == 10
        assert len(data_value) == 10

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出—无page num")
    def test_data_cleaning_details_without_page_num(self):
        """
        验证数据源列表—空case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_list_without_page_num().json()
        data_value = json_data["data"]["data"]
        count = json_data["data"]["count"]
        page_size = json_data["data"]["pageSize"]
        total_pages = json_data["data"]["totalPages"]
        assert page_size == 100
        assert total_pages == 1
        assert count == 10
        assert len(data_value) == 10

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情-schema校验")
    def test_data_cleaning_output_details_schema_check(self):
        json_data = dc.get_data_cleaning_details_jsonschema().json()
        validate(json_data, schema=data_cleaning_details_schema)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—有效case_id参数")
    def test_data_cleaning_details_by_valid_case_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_jsonschema().json()
        data_value = json_data["data"]
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—case_id参数为空")
    def test_data_cleaning_details_by_none_case_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_by_none_caseid().json()
        data_value = json_data["data"]
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—无case_id参数")
    def test_data_cleaning_details_without_case_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_by_none_caseid().json()
        data_value = json_data["data"]
        assert len(data_value)

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—无效data_id参数")
    def test_data_cleaning_details_invalid_data_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_by_invalid_data_id().json()
        code_value = json_data["code"]
        data_value = json_data["data"]
        assert code_value == 3000
        assert data_value is None

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—无data_id参数")
    def test_data_cleaning_details_without_data_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_without_data_id().json()
        code_value = json_data["code"]
        data_value = json_data["data"]
        assert code_value == 9997
        assert data_value is None

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—data_id参数值为空")
    def test_data_cleaning_details_none_data_id(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_by_none_data_id().json()
        code_value = json_data["code"]
        data_value = json_data["data"]
        assert code_value == 9997
        assert data_value is None

    @pytest.mark.DataCleaning
    @allure.story("数据清洗输出详情—非法参数值")
    def test_data_cleaning_details_invalid_params(self):
        """
        验证数据源列表—有效case_id；
        校验状态码
        """
        json_data = dc.get_data_cleaning_details_by_invalid_params().json()
        code_value = json_data["code"]
        data_value = json_data["data"]
        assert code_value == 9997
        assert data_value is None
