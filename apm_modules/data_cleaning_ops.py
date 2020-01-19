# !/usr/bin/env python3
#coding=utf-8
'''
@File   :data_cleaning_ops.py
@Author :zhumeng
@Date   :2020/1/7  16:20
@Version:1.0
@Desc   : 数据清洗动作
'''

import json
from common import configHTTP
from common.getData import GetData

cf = configHTTP.ConfigHttp()


class DataCleaningOps():

    '''
    @Author : zhumeng
    @Desc   :
    @param  :
    '''
    def alter_data(self,dataType,dataDirName):
        str_data_Type = uploadData_json['dataSetModelStr']
        str_data_Type = str_data_Type[:13] + dataType + str_data_Type[17:]
        uploadData_json['dataSetModelStr'] = str_data_Type[:79] + dataDirName + str_data_Type[-2:]
        # str_data_Type = uploadData_json['dataSetModelStr']
        # uploadData_json['dataSetModelStr']=str_data_Type.replace('实体识别',dataType)
        # str_data_Type=uploadData_json['dataSetModelStr']
        # str_data= str_data_Type.replace('接口自动化—生死疲劳已标注.txt', dataDirName)
        return uploadData_json['dataSetModelStr']
