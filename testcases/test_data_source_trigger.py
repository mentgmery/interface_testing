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



clean_data={
            "name": "清洗",
            "alias": "clean",
            "type": "page",
            "paramsdata": {
                "case_id" : "817845123",
                "sDid" : "7E06FACE-0921-472F-BF52-C070750544D4"
        },
        "url": "http://192.168.1.78:8018/dataetl",
        "desc": '跳转到数据清洗页面，弹出表头选定的弹窗'
      }


skip_clean_data = {
        "name": "跳过清洗",
        "alias": "skip-clean",
        "type": "page",
        "paramsdata": {
          "case_id": '817845123',
          "sDid": '7E06FACE-0921-472F-BF52-C070750544D4',
          "is_jump": 'true'
        },
        "url": "http://192.168.1.78:8018/dataetl",
        "desc": "跳转到数据清洗页面，弹出跳过清洗的弹窗"
      }

@allure.feature("数据源—触发器")
@pytest.mark.usefixtures('driver_setup')
class TestDataSourceTrigger():

    @pytest.mark.DataSource
    @allure.story("数据源—清洗—触发器-非空")
    def test_datasource_clean_trigger(self):
        """
        验证数据源清洗触发器，ENV_ACTION_CLEAN非空，页面id为__data_source_etl元素是否存在
        """
        dst = DataSourceTrigger(self.driver) # 打开浏览器
        url=dst.get_datasource_trigger_clean_url(clean_data) # 获取数据源触发器—清洗—url
        print(url)
        boolean_value=dst.datasource_trigger_url(url,'__data_source_etl') #打开url地址，获取id为__data_source_etl的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataSource
    @allure.story("数据源—清洗—触发器-空")
    def test_datasource_null_clean_trigger(self):
        """
        验证数据源清洗触发器，ENV_ACTION_CLEAN为空，页面id为__data_source_etl元素是否存在
        """
        dst = DataSourceTrigger(self.driver) # 打开浏览器
        url=dst.get_datasource_trigger_clean_url(None) # 获取数据源触发器—清洗—url
        print(url)
        boolean_value=dst.datasource_trigger_url(url,'__data_source_etl') #打开url地址，获取id为__data_source_etl的元素是否存在，返回布尔值
        assert boolean_value == False


    @pytest.mark.DataSource
    @allure.story("数据源—跳过清洗—触发器-非空")
    def test_datasource_skip_clean_trigger(self):
        """
        验证数据源跳过清洗触发器，ENV_ACTION_SKIP_CLEAN非空，页面id为__data_source_jumpetl元素是否存在
        """
        dst = DataSourceTrigger(self.driver) # 打开浏览器
        url=dst.get_datasource_trigger_skip_clean_url(skip_clean_data) # 获取数据源触发器—跳过清洗—urlk
        print(url)
        boolean_value=dst.datasource_trigger_url(url,'__data_source_jumpetl') #打开url地址，获取id为__data_source_jumpetl的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataSource
    @allure.story("数据源—跳过清洗—触发器-空")
    def test_datasource_null_skip_clean_trigger(self):
        """
        验证数据源跳过清洗触发器，ENV_ACTION_SKIP_CLEAN为空，页面id为__data_source_jumpetl元素是否存在
        """
        dst = DataSourceTrigger(self.driver) # 打开浏览器
        url=dst.get_datasource_trigger_skip_clean_url(None) # 获取数据源触发器—跳过清洗—url
        boolean_value=dst.datasource_trigger_url(url,'__data_source_jumpetl') #打开url地址，获取id为__data_source_jumpetl的元素是否存在，返回布尔值
        assert boolean_value == False