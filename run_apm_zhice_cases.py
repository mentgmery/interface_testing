# !/usr/bin/env python3
#coding=utf-8
'''
智语2.0线上
'''
import configparser,os.path
import os,subprocess
from common.setCookie import Set_Cookie
current_path = os.path.abspath(__file__)
from common.logger import Logger
logger = Logger(logger="run_apm_zhice_Test").get_log()


#读写config.ini文件，初始化修改URL地址，区分线上和测试环境。
def modify_config_file():
    # 读取配置文件
    config = configparser.ConfigParser()
    proDir = os.path.abspath(os.path.dirname((__file__)))
    configPath = proDir + '/testfiles/config_file/config.ini'
    path = os.path.abspath(configPath)
    config.read(path, encoding="utf-8")
    config.set("testServer","url","http://192.168.1.244:8881")#修改测试地址
    # 写入
    config.write(open(path, "w", encoding="utf-8"))


def init_run_apm_zhice_Test():
    cmd = "python3 -m pytest -sq --reruns 1 testcases --alluredir report/xml"
    subprocess.call(cmd, shell=True)
    logger.info("执行APM智策接口自动化测试")


def init_report():
    cmd = "allure generate --clean report/html report/xml -o report/html"
    subprocess.call(cmd, shell=True)
    report_path = "/report/html/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


if __name__ == "__main__":
    Set_Cookie().set_cookie_config()
    modify_config_file()
    init_run_apm_zhice_Test()
    init_report()
