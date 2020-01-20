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
from apm_modules.data_cleaning_output import DataCleaningOutput

@allure.feature("数据清洗动作")
class TestDataCleaningOps():

    @pytest.mark.testENV
    @allure.story("schema结构校验")
    def data_cleaning_ops_schema_check(self):
        pass

    def test_01(self):
        pass