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


data_cleaning_list_schema = GetData().read_schema_file('data_cleaning_list.schema')


@allure.feature("数据清洗")
class TestDataCleaningOutput():

    @allure.story("数据清洗")
    def test_data_cleaning_schema_check(self):
        pass

    def test_01(self):
        pass