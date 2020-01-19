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
from apm_modules.template_mgt_ops import TemplateMgtOps
from apm_modules.template_mgt_output import TemplateMgtOutput


class TestDataSourceOutput():

    #测试本地上传文件
    @pytest.mark.parametrize("filename,dataType,dataDirName",upload_parametrize)
    @pytest.mark.run(order=1)
    def test_upload_file(self,filename,dataType,dataDirName):
        json = TemplateMgt().upload_file(filename,dataType,dataDirName)
        assert json['code'] == 200
