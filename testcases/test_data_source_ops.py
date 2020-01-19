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
from apm_modules.data_source_ops import DataSourceOps

url="http://www.baidu.com"

@allure.feature("数据源—动作")
@pytest.mark.usefixtures('driver_setup')
class TestDataSource_OPS():

    @pytest.mark.DataSource
    @allure.feature("数据源动作")
    def test_data_source_ops(self):
        ds=DataSourceOps(self.driver)
        assert ds.datasource_add_data(url) == True
