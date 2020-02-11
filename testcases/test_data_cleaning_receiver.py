# !/usr/bin/env python3
#coding=utf-8
'''
@File   :test_data_cleaning_receiver.py
@Author :lianfeng
@Date   :2020/1/21 11:13 AM
@Version:1.0
@Desc   : 数据清理—接收器 验证
'''
import allure,pytest

from apm_modules.data_cleaning_receiver import DataCleaningReceiver

data_source_list ={
        "name" : "数据文件列表",
        "alias" : "data-list",
        "getMethods" : {
          "type" : "API",
          "url" : "http://192.168.1.78:8016/api/data_source",
          "parameter" : {
            "q_type": {
              "type": "Number",
              "default": 0
            },
            "page_size": 10,
            "page": 1,
            "case_id": "817845123"
          }
        },
        "getContents": {
          "category": '数据源/数据文件',
          "fields": {
          }
        }
      }

data_source_details = {
        "data-detail": {
        "name": "数据文件详情",
        "alias": "data-detail",
        "getMethods": {
          "type": "API",
          "url": "http://192.168.1.78:8016/lensData/lensData/getRawData",
          "parameter": {
            "id" : "7E06FACE-0921-472F-BF52-C070750544D4",
            "case_id" : "817845123"
          }
        },
        "getContents": {
          "category": "数据源/数据文件详情",
          "fields": {

          }
        }
      }
    }

template_list = {
      "data-list": {
        "name" : "模板文件列表",
        "alias" : "data-list",
        "getMethods": {
          "type" : 'API',
          "url" : 'http://192.168.1.78:8017/api/template',
          "parameter" : {
            "page_size" : {
              "type" : "Number",
              "default" : 100
            }
          }
        },
        "getContents": {
          "category": "数据源/数据文件",
          "fields": {
          }
        }
      }
    }

template_details =  {"data-detail": {
        "name": "模板文件详情",
        "alias": "data-detail",
        "getMethods": {
          "type": "API",
          "url": "http://192.168.1.78:8017/template",
          "parameter": {
            "temp_id": {
              "type": "String",
              "default": "971430007"
            }
          }
        },
        "getContents": {
          "category": "数据源/数据文件详情",
          "fields": {
          }
        }
      }
    }


@allure.feature("数据清洗—接收器")
@pytest.mark.usefixtures('driver_setup')
class TestDataCleaningReceiver():

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—数据列表—接收器-非空")
    def test_datacleaning_receiver_data_list_url(self):
        """
        验证数据清洗—接收器—数据列表，ENV_OUTPUT_TEMPLATE_LIST非空，页面id为__data_source_list元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_dataclean_receiver_datalist_url(data_source_list)  # 获取数据源触发器—新增数据url
        print(url)
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_source_list') # 打开url地址，获取id为__data_source_list的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—数据列表—接收器-空")
    def test_datacleaning_receiver_null_data_list_url(self):
        """
        验证数据清洗—接收器—数据列表，ENV_OUTPUT_TEMPLATE_LIST为空，页面id为__data_source_list元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_dataclean_receiver_datalist_url(None)  # 获取数据源触发器—新增数据url
        print(url)
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_source_list') # 打开url地址，获取id为__data_source_list的元素是否存在，返回布尔值
        assert boolean_value == False

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—数据详情—接收器—非空")
    def test_datacleaning_receiver_data_details_url(self):
        """
        验证数据清洗—接收器—数据列表，ENV_OUTPUT_DATA_DETAIL非空，页面id为__data_source_detail元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_dataclean_receiver_datadetails_url(data_source_details)  # 获取数据源触发器—新增数据url
        print(url)
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_source_detail') # 打开url地址，获取id为__data_source_detail的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—数据详情—接收器—空")
    def test_datacleaning_receiver_null_data_details_url(self):
        """
        验证数据清洗—接收器—数据列表，ENV_OUTPUT_DATA_DETAIL为空，页面id为__data_source_detail元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_dataclean_receiver_datadetails_url(None)  # 获取数据源触发器—新增数据url
        print(url)
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_source_detail') # 打开url地址，获取id为__data_source_detail的元素是否存在，返回布尔值
        assert boolean_value == False

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—模板列表—接收器—非空")
    def test_datacleaning_receiver_template_list_url(self):
        """
        验证数据清洗—接收器—模板列表，ENV_OUTPUT_DATA_LIST非空，页面id为__data_template-list元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_template_list_url(template_list)  # 获取数据源触发器—新增数据url
        print(url)
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_template_list') # 打开url地址，获取id为__data_template-list的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—模板列表—接收器—空")
    def test_datacleaning_receiver_null_template_list_url(self):
        """
        验证数据清洗—接收器—模板列表，ENV_OUTPUT_DATA_LIST为空，页面id为__data_template-list元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_template_list_url(None)  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_template_list') # 打开url地址，获取id为__data_template-list的元素是否存在，返回布尔值
        assert boolean_value == False

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—模板详情—接收器-非空")
    def test_datacleaning_receiver_template_details_url(self):
        """
        验证数据清洗—接收器—模板详情，ENV_OUTPUT_DATA_DETAIL非空，页面id为__data_template-detail元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_template_details_url(template_details)  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_template-detail') # 打开url地址，获取id为__data_template-detail的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—模板详情—接收器-空")
    def test_datacleaning_receiver_null_template_details_url(self):
        """
        验验证数据清洗—接收器—模板详情，ENV_OUTPUT_DATA_DETAIL为空，页面id为__data_template-detail元素是否存在
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_template_details_url(None)  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_template-detail') # 打开url地址，获取id为__data_template-detail的元素是否存在，返回布尔值
        assert boolean_value == False