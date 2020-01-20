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

@allure.feature("数据源—动作")
@pytest.mark.usefixtures('driver_setup')
class TestDataSource_OPS():

    @pytest.mark.DataSource
    @allure.story("数据源—动作—新增数据")
    def test_data_source_ops(self):
        pass
        # ds=DataSourceOps(self.driver)
        # url = ds.get_datasource_add_data_url() # 获取数据源url
        # assert ds.datasource_add_data(url) == True
