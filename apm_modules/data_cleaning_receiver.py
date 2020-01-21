# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_receiver.py
@Author :lianfeng
@Date   :2020/1/21 9:04 AM
@Version:1.0
@Desc   :  数据清洗接收器
'''
from apm_modules.data_source_output import DataSourceOutput
from apm_modules.template_mgt_output import TemplateMgtOutput
from common.openbrowser import OpenURL

data_source_list ={
      "data-list": {
        "name" : "数据文件列表",
        "alias" : "data-list",
        "getMethods" : {
          "type" : "API",
          "url" : "{{ APP_HOST }}/api/data_source",
          "parameter" : {
            "q_type": {
              "type": "Number",
              "default": 0
            },
            "page_size": 10,
            "page": 1,
            "case_id": "442791611"
          }
        },
        "getContents": {
          "category": '数据源/数据文件',
          "fields": {
          }
        }
      }
    }

data_source_details = {
        "data-detail": {
        "name": "数据文件详情",
        "alias": "data-detail",
        "getMethods": {
          "type": "API",
          "url": "{{ APP_HOST }}/lensData/lensData/getRawData",
          "parameter": {
            "id" : "3DA23E9F-F386-4A0D-87B1-25FFCD06A80D",
            "case_id" : "442791611"
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
          "url" : '{{ APP_HOST }}/api/template',
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
          "url": "{{ APP_HOST }}/api/template",
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

class DataCleaningReceiver(OpenURL):

    def datacleaning_receiver_url(self,url,requiredDom):
        """
        数据清洗—接收器，访问url获取元素值
        :param url: 接收器请求接口后，访问url地址
        :param requiredDom: Dom树中id值
                数据文件列表：'__data_source_list'
                数据文件详情：'__data_source_detail'
                模板列表：'__data_template-list'
                模板详情：'__data_template-detail'
        :return: 布尔，True/False;存在/不存在
        """
        self.driver.get(url)
        value = self.driver.find_element_by_id(requiredDom).is_displayed() # 取什么值自己定位元素
        return value


    def get_dataclean_receiver_datalist_url(self):
        """获取接收器—模板列表url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/data_source?params=xxx
        """
        tmo_url = TemplateMgtOutput().templateMgt_list_validity().url
        url = tmo_url + '&ENV_OUTPUT_TEMPLATE_LIST=' + str(template_list)
        return url

    def get_dataclean_receiver_datadetails_url(self):
        """获取接收器—模板详情url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/data_source?params=xxx
        """
        tmo_url = TemplateMgtOutput().templateMgt_details_validity().url
        url = tmo_url + '&ENV_OUTPUT_DATA_DETAIL=' + str(template_details)
        return url

    def get_template_list_url(self):
        """获取接收器—数据文件列表url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/template?params=xxx
        """
        dso_url = DataSourceOutput().datasource_list_validity().url
        url = dso_url + '&ENV_OUTPUT_DATA_LIST=' + str(data_source_list)
        return url

    def get_template_details_url(self):
        """获取接收器—数据文件详情url
        :return: 返回请求的url 示例：http://192.168.1.244:8881/api/template?params=xxx
        """
        dso_url = DataSourceOutput().datasource_details_validity().url
        url = dso_url + '&ENV_OUTPUT_DATA_DETAIL=' + str(data_source_list)
        return url