# !/usr/bin/env python3
#coding=utf-8
'''
@File   : data_source_trigger.py
@Author : lianfeng
@Date   : 2020/1/19 5:16 PM
@Version: 1.0
@Desc   : 数据源—触发器 共3条
'''
from common import configHTTP
from common.openbrowser import OpenURL

cf = configHTTP.ConfigHttp()

#dataSource_url = "xxxxx"
dataSource_url = "/api/template"

class DataSourceTrigger(OpenURL):

    def datasource_trigger_rinse_url(self,func,url):
        """
        数据源—触发器，打开浏览器，访问url获取元素值
        :param func: 要调用的触发器函数名
        :param url: 触发器请求接口后，访问url地址
        :return: 特定元素的属性值。
        """
        self.driver.get(url)
        #self.driver.page_source
        func()
        id_value = self.driver.find_element_by_id('su').get_attribute("value") # 取什么值自己定位元素
        #visible = self.driver.find_element_by_id('su').is_displayed() # 取什么值自己定位元素
        return id_value

    def datasource_trigger_rinse_validity(self):
        """
        正向的数据源—清洗—触发器,请求值均正常。
        Returns: get请求的结果
        """
        dict_data = {
                    "page_size" : 100,
                    "page" : 1,
                    "case_id" : '442791611'
                    }
        cf.set_url(dataSource_url)
        cf.set_params(dict_data)
        cf.set_headers(None)
        print('执行trigger')
        return cf.get()
        # dict_data =  {
        #             "sDid" : '908651985'
        #             }
        # cf.set_url(dataSource_url)
        # cf.set_data(dict_data)
        # cf.set_headers(None)
        # print('执行trigger')
        # return cf.post()

    def datasource_trigger_rinse_invalid_sDid(self):
        """
        正向的数据源—清洗—触发器,无效的sDid
        Returns: post请求的结果
        """
        dict_data =  {
                    "sDid" : 'jkdlajfkl'
                    }
        cf.set_url(dataSource_url)
        cf.set_data(dict_data)
        cf.set_headers(None)
        return cf.post()


    def datasource_trigger_rinse_null_sDid(self):
        """
        正向的数据源—清洗—触发器，空的sDid
        Returns: post请求的结果
        """
        dict_data =  {
                    "sDid" : ''
                    }
        cf.set_url(dataSource_url)
        cf.set_data(dict_data)
        cf.set_headers(None)
        return cf.post()