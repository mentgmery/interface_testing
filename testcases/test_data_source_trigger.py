# !/usr/bin/env python3
#coding=utf-8

'''
@File   :test_data_source_trigger.py
@Author :lianfeng
@Date   :2020/1/19 6:06 PM
@Version:1.0
@Desc   : 数据源—清洗和跳过清洗—触发器校验，共两条测试用例
'''

import allure,pytest
from apm_modules.data_source_trigger import DataSourceTrigger

@allure.feature("数据源—触发器")
@pytest.mark.usefixtures('driver_setup')
class TestDataSourceTrigger():

    @pytest.mark.DataSource
    @allure.story("数据源—清洗—触发器")
    def test_datasource_clean_trigger(self):
        """
        验证数据源清洗触发器，是否存在id为__data_source_etl元素
        """
        dst = DataSourceTrigger(self.driver) # 打开浏览器
        url=dst.get_datasource_trigger_clean_url() # 获取数据源触发器—清洗—url
        boolean_value=dst.datasource_trigger_url(url,'__data_source_etl') #打开url地址，获取id为__data_source_etl的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataSource
    @allure.story("数据源—跳过清洗—触发器")
    def test_datasource_skip_clean_trigger(self):
        """
        验证数据源跳过清洗触发器，是否存在id为__data_source_jumpetl元素
        """
        dst = DataSourceTrigger(self.driver) # 打开浏览器
        url=dst.get_datasource_trigger_skip_clean_url() # 获取数据源触发器—跳过清洗—url
        boolean_value=dst.datasource_trigger_url(url,'__data_source_jumpetl') #打开url地址，获取id为__data_source_jumpetl的元素是否存在，返回布尔值
        assert boolean_value == True

