# !/usr/bin/env python3
#coding=utf-8

'''
@File   :test_data_source_trigger.py
@Author :lianfeng
@Date   :2020/1/19 6:06 PM
@Version:1.0
@Desc   : 数据源触发器验证
'''

import allure,pytest
from apm_modules.data_source_trigger import DataSourceTrigger

rinse_url = "http://www.baidu.com"

@allure.feature("数据源—触发器")
@pytest.mark.usefixtures('driver_setup')
class TestDataSourceTrigger():

    @pytest.mark.DataSource
    @allure.feature("数据源—清洗—触发器—正确数据")
    def test_datasource_trigger_validity(self):
        dst = DataSourceTrigger(self.driver)
        r_data = dst.datasource_trigger_rinse_validity()
        print(r_data.status_code)
        #print(r_data.json())
        assert dst.datasource_trigger_rinse_url(rinse_url) == '百度一下'

    @pytest.mark.DataSource
    @allure.feature("数据源—清洗—触发器—无效的请求")
    def test_datasource_trigger_invalid_sDid(self):
        dst = DataSourceTrigger(self.driver)
        r_data = dst.datasource_trigger_rinse_invalid_sDid()
        print(r_data.status_code)
        #print(r_data.json())
        assert dst.datasource_trigger_rinse_url(url) == '百度一下'

    @pytest.mark.DataSource
    @allure.feature("数据源—清洗—触发器—空的请求")
    def test_datasource_trigger_null_sDid(self):
        dst = DataSourceTrigger(self.driver)
        r_data = dst.datasource_trigger_rinse_null_sDid()
        print(r_data.status_code)
        #print(r_data.json())
        assert dst.datasource_trigger_rinse_url(url) == '百度一下'