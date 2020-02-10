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


add_data = {
        "add": {
        "name": "新增数据",
        "alias": "add",
        "type" : 'window',
        "metadata": {
        },
        "url": "http://192.168.1.78:8016/filemanagement?case_id=817845123",
        "desc": '其他应用触发【新增数据】动作时，弹出【新增数据】window（小窗口），在小窗口中完成新增数据，触发父级页面刷新'
      }
    }

@allure.feature("数据清洗—触发器")
@pytest.mark.usefixtures('driver_setup')
class TestDataCleaningTrigger():

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—新增数据—触发器-非空")
    def test_datacleaning_trigger_url(self):
        """
        验证数据源清洗触发器，ENV_ACTION_ADD非空，页面id为__data_source_jumpetl元素是否存在
        """
        dct = DataCleaningTrigger(self.driver)  # 打开浏览器
        url = dct.get_datacleaning_trigger_add_data_url(add_data)  # 获取数据源触发器—新增数据url
        boolean_value = dct.datacleaning_trigger_url(url,'__data_source_adddata') # 打开url地址，获取id为__data_source_jumpetl的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—新增数据—触发器-空")
    def test_datacleaning_null_trigger_url(self):
        """
        验证数据源清洗触发器，ENV_ACTION_ADD为空，页面id为__data_source_jumpetl元素是否存在
        """
        dct = DataCleaningTrigger(self.driver)  # 打开浏览器
        url = dct.get_datacleaning_trigger_add_data_url(None)  # 获取数据源触发器—新增数据url
        boolean_value = dct.datacleaning_trigger_url(url,'__data_source_adddata') # 打开url地址，获取id为__data_source_jumpetl的元素是否存在，返回布尔值
        assert boolean_value == False