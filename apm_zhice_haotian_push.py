# !/usr/bin/env python3
#coding=utf-8
import os, jenkins, json
import requests
'''
获取jenkins构建信息和本次报告地址，创建变量保存。
'''
jenkins_url="http://192.168.1.176:8090/" #jenkins登录地址
server = jenkins.Jenkins(jenkins_url, username='lianfeng', password='elensdata')
# print(server.jobs_count())
job_name="job/jTest-testing-automation-apm_test_driven/" # job名称
job_url=jenkins_url+job_name # job的url地址
job_last_number=server.get_info(job_name)['lastBuild']['number'] # 获取最后一次构建
# print(job_last_number)
# print(job_url)
report_url=job_url+str(job_last_number)+'/allure' # 报告地址
# print(report_url)
'''
钉钉推送方法：
读取report文件中"prometheusData.txt"，循环遍历存储为字典，从字典中获取需要的值。
使用钉钉机器人的接口，拼接后推送text
'''


def dd_push(url):
    d = {}
    proDir = os.path.abspath(os.path.dirname((__file__)))
    f = open(proDir + '/report/html/export/prometheusData.txt', 'r')
    for lines in f:
        # lines.strip('\n').replace(' ', '').replace('、', '/').replace('?', '').split(' ')
        for c in lines:
            launch_name = lines.strip('\n').split(' ')[0]
            num = lines.strip('\n').split(' ')[1]
            d.update({launch_name: num})
    f.close()
    retries_run = d.get('launch_retries_run')  # 运行总数
    status_passed = d.get('launch_status_passed')  # 通过数量
    status_failed = d.get('launch_status_failed')  # 不通过数量
    '''
    钉钉推送
    '''
    con={"msgtype":"text",
         "text":{"content":"昊天APM接口自动化脚本执行完成。\n测试概述:\n运行总数:"+retries_run+"\n通过数量:"+status_passed+"\n失败数量:"+status_failed+"\n构建地址：\n"+job_url+"\n报告地址：\n"+report_url}
         }

    requests.post(url,data=json.dumps(con),headers={'Content-Type':'application/json'})


if __name__ == '__main__':
    apm_test_group = 'https://oapi.dingtalk.com/robot/send?access_token=46fa45901474dcb529094b1716ab54894730edcc300c6a85aa3e0b5923444578' #测试组
    apm_group = 'https://oapi.dingtalk.com/robot/send?access_token=0536de662e39c93a7112af7aacfd19c95125188bf1b6fbb19271d31e49fc045a'
    dd_push(apm_test_group)
    dd_push(apm_group)
