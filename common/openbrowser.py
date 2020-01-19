# !/usr/bin/env python3
#coding=utf-8
'''
@File   :openbrowser.py
@Author :lianfeng
@Date   :2020/1/19 1:58 PM
@Version:1.0
@Desc   : 打开浏览器-录入URL
'''
import selenium
from selenium.webdriver import DesiredCapabilities


class OpenURL(object):

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://192.168.1.176:5001/wd/hub",
                                                               desired_capabilities=DesiredCapabilities.CHROME)
        driver.maximize_window()

        return driver

    def quit_browser(self):
        self.driver.quit()