import unittest
from BeautifulReport import BeautifulReport
import os

""""
@project:AppUIAuto
@author:lenovo
@file:report.py
@ide:PyCharm
@time:2019/6/12 11:24
@month:六月

"""
"""
封装BeautifulReport  实现参数可配置
报告目录默认为Reports目录
"""


def run_all(description, filename, report_path=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if report_path:
        case_dir = report_path
    else:
        case_dir = base_dir + '\\Reports\\'
    testsuit = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
    result = BeautifulReport(testsuit)
    result.report(description='手机端测试报告', filename='xxxApp自动化测试报告', log_path=case_dir)
    result.report(description=description, filename=filename, log_path=case_dir)
