# !/usr/bin/env python3
#coding=utf-8
'''
@File   :test_data_source.py
@Author :zhumeng
@Date   :2020/1/7下午3:20
@Version:1.0
@Desc   :
'''
import pytest, allure
from apm_modules.data_cleaning_ops import DataCleaningOps


class TestDataSourceOutput():

    #测试本地上传文件
    @pytest.mark.TemplateMgt
    @allure.feature("模板列表—schema结构校验")
    def test_upload_file(self,filename,dataType,dataDirName):
        pass
