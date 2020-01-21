# !/usr/bin/env python3
#coding=utf-8
'''
@File   :test_data_cleaning_trigger.py
@Author :lianfeng
@Date   :2020/1/20 11:08 PM
@Version:1.0
@Desc   : 数据清洗—新增数据—触发器验证 1条用例
'''
import allure,pytest

from apm_modules.data_cleaning_trigger import DataCleaningTrigger


@allure.feature("数据清洗—触发器")
@pytest.mark.usefixtures('driver_setup')
class TestDataCleaningTrigger():

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—新增数据—触发器")
    def test_datacleaning_trigger_url(self):
        """
                验证数据源清洗触发器，是否存在id为__data_source_jumpetl元素
                """
        dct = DataCleaningTrigger(self.driver)  # 打开浏览器
        url = dct.get_datacleaning_trigger_add_data_url()  # 获取数据源触发器—新增数据url
        boolean_value = dct.datacleaning_trigger_url(url,'__data_source_jumpetl') # 打开url地址，获取id为__data_source_jumpetl的元素是否存在，返回布尔值
        assert boolean_value == True