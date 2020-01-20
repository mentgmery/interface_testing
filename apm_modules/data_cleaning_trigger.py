# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_trigger.py
@Author :lianfeng
@Date   :2020/1/20 10:54 PM
@Version:1.0
@Desc   : 数据清洗—新增数据—触发器
'''
from apm_modules.data_source_ops import DataSourceOps
from common.openbrowser import OpenURL


add_data = {
        "add": {
        "name": "新增数据",
        "alias": "add",
        "type" : 'window',
        "metadata": {
        },
        "url": "http://admin.gongan.corp.elensdata.com/filemanagement?case_id=442791611",
        "desc": '其他应用触发【新增数据】动作时，弹出【新增数据】window（小窗口），在小窗口中完成新增数据，触发父级页面刷新'
      }
    }

class DataCleaningTrigger(OpenURL):

    def datacleaning_trigger_url(self,url,requiredDom):
        """
        数据源—触发器，打开浏览器，访问url获取元素值
        :param url: 触发器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                新增数据：'__data_source_jumpetl'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        # self.driver.page_source
        value = self.driver.find_element_by_id(requiredDom).is_displayed()  # 取什么值自己定位元素
        # visible = self.driver.find_element_by_id('su').is_displayed() # 取什么值自己定位元素
        return value


    def get_datacleaning_trigger_add_data_url(self):
        """
        获取数据清洗触发器—url
        Returns: 返回get的url 示例：http://192.168.1.244:8881/dataetl?case_id=xxxx&sDid=xxxx&ENV_ACTION_ADD=xxxx
        """
        add_data_url=DataSourceOps(self.driver).get_datasource_add_data_url() # 获取数据源动作—新增数据url
        url = add_data_url + '&ENV_ACTION_ADD' + str(add_data)
        return url