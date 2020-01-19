# !/usr/bin/env python3
#coding=utf-8
'''
@File   :test_data_source.py
@Author :zhumeng
@Date   :2020/1/7下午3:20
@Version:1.0
@Desc   : 数据源输出验证 共16条
'''
import allure,pytest
from jsonschema import validate
from apm_modules.data_source_output import DataSourceOutput
from common.getData import GetData

ds = DataSourceOutput()

datasource_list_schema = GetData().read_schema_file('data_source_list.schema')
#datasource_details_schema = GetData().read_schema_file('datasource_details.schema')
@allure.feature("数据源—输出")
class TestDataSourceOutput():

    @pytest.mark.DataSource
    @allure.feature("数据源列表—schema结构校验")
    def test_datasource_list_schema_check(self):
        json_data=ds.datasource_list_validity().json()
        validate(json_data,schema=datasource_list_schema)


    @pytest.mark.DataSource
    @allure.feature("数据源列表—正确数据")
    def test_datasource_list_validity(self):
        """
        验证数据源列表—正确数据返回值；
        校验状态码
        """
        r_data=ds.datasource_list_validity()
        s_code = r_data.status_code
        assert s_code == 200

    @pytest.mark.DataSource
    @allure.feature("数据源列表—无效的case_id")
    def test_datasource_list_invalid_case_id(self):
        """
        验证数据源列表—无效case_id；
        校验状态码和code码
        """
        r_data=ds.datasource_list_invalid_case_id()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—无效的page")
    def test_datasource_list_invalid_page(self):
        """
        验证数据源列表—无效page；
        校验状态码和code码
        """
        r_data=ds.datasource_list_invalid_page()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—无效的pagesize")
    def test_datasource_list_invalid_page_size(self):
        """
        验证数据源列表—无效pagesize；
        校验状态码和code码
        """
        r_data=ds.datasource_list_invalid_page_size()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—无效的q_type")
    def test_datasource_list_invalid_q_type(self):
        """
        验证数据源列表—无效q_type；
        校验状态码和code码
        """
        r_data=ds.datasource_list_invalid_q_type()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—空的case_id")
    def test_datasource_list_null_case_id(self):
        """
        验证数据源列表—空的case_id；
        校验状态码和code码
        """
        r_data=ds.datasource_list_null_case_id()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—空的page")
    def test_datasource_list_null_page(self):
        """
        验证数据源列表—空的page；
        校验状态码和code码
        """
        r_data=ds.datasource_list_null_page()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—空的page_size")
    def test_datasource_list_null_page_size(self):
        """
        验证数据源列表—空的page_size；
        校验状态码和code码
        """
        r_data=ds.datasource_list_null_page_size()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源列表—空的q_type")
    def test_datasource_list_null_q_type(self):
        """
        验证数据源列表—空的q_type；
        校验状态码和code码
        """
        r_data=ds.datasource_list_null_q_type()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源详情—schema结构校验")
    def test_datasource_details_schema_check(self):
        json_data=ds.datasource_details_validity().json()
        validate(json_data,schema=datasource_details_schema)

    @pytest.mark.DataSource
    @allure.feature("数据源详情—正确数据")
    def test_datasource_details_validity(self):
        """
        验证数据源详情—正确数据返回值；
        校验状态码
        """
        r_data=ds.datasource_details_validity()
        s_code = r_data.status_code
        assert s_code == 200

    @pytest.mark.DataSource
    @allure.feature("数据源详情—无效的case_id")
    def test_datasource_details_invalid_case_id(self):
        """
        验证数据源详情—无效的case_id；
        校验状态码和code码
        """
        r_data=ds.datasource_details_invalid_case_id()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源详情—无效的data_id")
    def test_datasource_details_invalid_data_id(self):
        """
        验证数据源详情—无效的data_id；
        校验状态码和code码
        """
        r_data=ds.datasource_details_invalid_data_id()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源详情—空的case_id")
    def test_datasource_details_null_case_id(self):
        """
        验证数据源详情—空的case_id；
        校验状态码和code码
        """
        r_data=ds.datasource_details_invalid_case_id()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0

    @pytest.mark.DataSource
    @allure.feature("数据源详情—空的data_id")
    def test_datasource_details_invalid_data_id(self):
        """
        验证数据源详情—空的data_id；
        校验状态码和code码
        """
        r_data=ds.datasource_details_null_data_id()
        s_code = r_data.status_code
        code = r_data.json()['code']
        assert s_code == 200
        assert code != 0