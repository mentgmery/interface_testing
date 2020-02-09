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
from apm_modules.data_cleaning_ops import DataCleaningOps


@allure.feature("数据清洗动作")
@pytest.mark.usefixtures('driver_setup')
class TestDataCleaningOps():

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—动作—清洗")
    def test_data_clean_ops(self):
        """
        验证访问清洗url，特定元素'__data_source_etl'是否存在
        """
        dc=DataCleaningOps(self.driver)
        url = dc.get_clean_url() # 获取清洗url
        assert dc.data_cleaning_ops(url, '__data_source_etl') is True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—动作—跳过清洗")
    def test_data_skip_clean_ops(self):
        """
        验证访问跳过清洗url，特定元素'__data_source_jumpetl'是否存在
        """
        dc=DataCleaningOps(self.driver)
        url = dc.get_skip_clean_url() # 获取跳过清洗url
        assert dc.data_cleaning_ops(url, '__data_source_jumpetl') is True
