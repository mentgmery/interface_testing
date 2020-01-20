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


@allure.feature("数据清洗—接收器")
@pytest.mark.usefixtures('driver_setup')
class TestDataCleaningReceiver():

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—数据列表—接收器")
    def test_datacleaning_receiver_data_list_url(self):
        """
        验证数据清洗—接收器—数据列表，是否存在id为__data_source_list元素
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_dataclean_receiver_datalist_url()  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_source_list') # 打开url地址，获取id为__data_source_list的元素是否存在，返回布尔值
        assert boolean_value == True

    @pytest.mark.DataCleaning
    @allure.story("数据清洗—数据列表—接收器")
    def test_datacleaning_receiver_data_details_url(self):
        """
        验证数据清洗—接收器—数据列表，是否存在id为__data_source_detail元素
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_dataclean_receiver_datadetails_url()  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_source_detail') # 打开url地址，获取id为__data_source_detail的元素是否存在，返回布尔值
        assert boolean_value == True

    def test_datacleaning_receiver_template_list_url(self):
        """
        验证数据清洗—接收器—数据列表，是否存在id为__data_template-listl元素
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_template_list_url()  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_template-list') # 打开url地址，获取id为__data_template-list的元素是否存在，返回布尔值
        assert boolean_value == True

    def test_datacleaning_receiver_template_details_url(self):
        """
        验证数据清洗—接收器—数据列表，是否存在id为__data_template-detail元素
        """
        dcr = DataCleaningReceiver(self.driver)  # 打开浏览器
        url = dcr.get_template_details_url()  # 获取数据源触发器—新增数据url
        boolean_value = dcr.datacleaning_receiver_url(url,'__data_template-detail') # 打开url地址，获取id为__data_template-detail的元素是否存在，返回布尔值
        assert boolean_value == True