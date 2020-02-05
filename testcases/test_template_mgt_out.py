# !/usr/bin/env python3
#coding=utf-8
'''
@File   :test_template_mgt.py
@Author :zhumeng
@Date   :2020/01/7下午2:57
@Version:1.0
@Desc   : 模型管理—模型列表/详情测试用例，当前共14条
'''

import pytest,allure
from jsonschema import validate
from apm_modules.template_mgt_output import TemplateMgtOutput
from common.getData import GetData

tm=TemplateMgtOutput()

template_mgt_list_schema = GetData().read_schema_file('template_mgt_list.schema')

template_mgt_details_schema = GetData().read_schema_file('template_mgt_details.schema')

@allure.feature("模板管理—输出")
class TestTemplateMgt():

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—schema结构校验")
    def test_template_mgt_list_schema_check(self):
        json_data = tm.templateMgt_list_validity().json()
        validate(json_data,schema=template_mgt_list_schema)

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—正确的数据")
    def test_templateMgt_list_validity(self):
        """
        验证模板列表—正确数据返回值；
        校验状态码，页面显示数据条数
        """
        r_data = tm.templateMgt_list_validity()
        s_code=r_data.status_code
        pagesize = r_data.json()['data']['pageSize']
        assert s_code == 200
        assert pagesize == 100


    @pytest.mark.TemplateMgt
    @allure.story("模板列表—无效的caseid")
    def test_templateMgt_list_invalid_caseid(self):
        """
        验证模板列表—无效的caseid；
        校验状态码
        """
        r_data = tm.templateMgt_list_invalid_caseid()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—caseid为空")
    def test_templateMgt_list_null_caseid(self):
        """
        验证模板列表—空的caseid；
        校验状态码
        """
        r_data = tm.templateMgt_list_null_caseid()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—无效的page")
    def test_templateMgt_list_invalid_page(self):
        """
        验证模板列表—无效的page；
        校验状态码
        """
        r_data = tm.templateMgt_list_invalid_page()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—空的page")
    def test_templateMgt_list_null_page(self):
        """
        验证模板列表—空的page；
        校验状态码
        """
        r_data = tm.templateMgt_list_null_page()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—无效的pagesize")
    def test_templateMgt_list_invalid_pagesize(self):
        """
        验证模板列表—无效的pagesize；
        校验状态码 != 200
        """
        r_data = tm.templateMgt_list_invalid_pagesize()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板列表—空的pagesize")
    def test_templateMgt_list_null_pagesize(self):
        """
        验证模板列表—空的pagesize；
        校验状态码
        """
        r_data = tm.templateMgt_list_null_pagesize()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板详情—schema结构校验")
    def test_templateMgt_details_schema(self):
        json_data = tm.templateMgt_details_validity().json()
        validate(json_data, schema=template_mgt_details_schema)

    @pytest.mark.TemplateMgt
    @allure.story("模板详情—正确的数据")
    def test_templateMgt_details_pagesize(self):
        """
        验证模板详情—正确数据返回值；
        校验状态码，其他数据等接口出来再定。
        """
        r_data = tm.templateMgt_details_validity()
        s_code=r_data.status_code
        #pagesize = r_data.json()['data']['pageSize']
        assert s_code == 200
        #assert pagesize == 100

    @pytest.mark.TemplateMgt
    @allure.story("模板详情—无效的temid")
    def test_templateMgt_details_invalid_temid(self):
        """
        验证模板详情—无效的caseid；
        校验状态码，其他数据等接口出来再定。
        """
        r_data = tm.templateMgt_details_invalid_temid()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板详情—空的temid")
    def test_templateMgt_details_details_null_temid(self):
        """
        验证模板详情—空的caseid；
        校验状态码，其他数据等接口出来再定。
        """
        r_data = tm.templateMgt_details_null_temid()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板详情—无效的caseid")
    def test_templateMgt_details_details_invalid_caseid(self):
        """
        验证模板详情—无效的caseid；
        校验状态码，其他数据等接口出来再定。
        """
        r_data = tm.templateMgt_details_invalid_caseid()
        s_code=r_data.status_code
        assert s_code == 200

    @pytest.mark.TemplateMgt
    @allure.story("模板详情—空的caseid")
    def test_templateMgt_details_details_null_caseid(self):
        """
        验证模板详情—空的caseid；
        校验状态码，其他数据等接口出来再定。
        """
        r_data = tm.templateMgt_details_null_caseid()
        s_code=r_data.status_code
        assert s_code == 200