# !/usr/bin/env python3
#coding=utf-8
'''
@File   :conftest.py
@Author :zhumeng
@Date   :2020/1/7上午15:00
@Version:1.0
@Desc   :  pytest配置文件
'''
import pytest
from common.openbrowser import OpenURL

@pytest.fixture()
def driver_setup(request):
    browser = OpenURL(request)
    request.instance.driver = browser.open_browser(request)
    def driver_teardown():
         request.instance.driver.quit()
    request.addfinalizer(driver_teardown)