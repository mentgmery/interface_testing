# !/usr/bin/env python3
#coding=utf-8
'''
@File   :configHTTP.py
@Author :lianfeng
@Date   :2019/9/16下午4:23
@Version:1.0
@Desc   : 重写post和get请求
'''
import json
import requests
from requests import ReadTimeout, RequestException
from common.getData import GetData
from common.logger import Logger
req_session = requests.session()

logger = Logger(logger="ConfigHttp").get_log()


class ConfigHttp:

    def set_url(self, url, inf_type):
        '''
        根据用户提供的项目名、端口号去判断项目的url拼接
        :param url:
        :return:
        '''
        self.url = GetData().get_apm_url(inf_type) + url

    def set_headers(self, header=None):
        '''
        设置请求头，默认取{'Cookie': cookie},遇到传json的接口会增加'Content-Type'
        :param header:
        :return:
        '''
        if header == 'json':
            header=GetData().get_cookie()
            header['Content-Type']='application/json;charset=UTF-8'
        elif header is None:
            header = GetData().get_cookie()
        elif header == 'text':
            header=GetData().get_cookie()
            header['Content-Type']='text/plain'
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # 定义一个get请求
    def get(self):
        try:
            self.response = requests.get(self.url, params=self.params,headers=self.headers, timeout=30)
            # response.raise_for_status()
            logger.info(self.response)
            return self.response
        except ReadTimeout as t_error:
            #self.logger.error("Time out!")
            raise Exception(t_error)
        except RequestException as error:
            #self.logger.error(response.text)
            raise Exception(error)
        except ValueError as v_error:
            #self.logger.error(ValueError)
            raise Exception(v_error)
        except NameError as name_error:
            #self.logger.error(NameError)
            raise Exception(name_error)
        except AttributeError as attr_error:
            #self.logger.error(AttributeError)
            raise Exception(attr_error)
        finally:
            req_session.close()

    # 定义一个post请求
    def post(self):
        try:
            self.response = requests.post(self.url, headers=self.headers, data=self.data, timeout=30)
            logger.info(self.response)
            return self.response
        except ReadTimeout as t_error:
            raise Exception(t_error)
        except RequestException as error:
            raise Exception(error)
        except ValueError as v_error:
            raise Exception(v_error)
        except NameError as name_error:
            raise Exception(name_error)
        except AttributeError as attr_error:
            raise Exception(attr_error)
        finally:
            req_session.close()

    # 定义一个发送参数中包含文件的post请求
    def postWithFile(self):
        try:
            self.response = requests.post(self.url, headers=self.headers,files=self.files,data=self.data,timeout=30)
            return self.response
        except ReadTimeout as t_error:
            raise Exception(t_error)
        except RequestException as error:
            raise Exception(error)
        except ValueError as v_error:
            raise Exception(v_error)
        except NameError as name_error:
            raise Exception(name_error)
        except AttributeError as attr_error:
                raise Exception(attr_error)
        finally:
            req_session.close()
