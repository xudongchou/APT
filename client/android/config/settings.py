"""
@project:code
@author:lenovo
@file:settings.py
@ide:PyCharm
@time:2019/7/18 14:50
@month:七月

"""
from appium import webdriver
# def config():
#     ip="192.168.186.128:7100"
#     device_suffix="/api/v1/devices"
#     prefix="http://"
#     port=7100
#     user_device_suffix="/api/v1/user/devices"
#     device_url=prefix+ip+device_suffix
#     user_device_url=prefix+ip+user_device_suffix
#     executor = 'http://127.0.0.1:4723/wd/hub'
#     return {
#         "ip":ip,
#         "device_url":device_url,
#         "user_device_url":user_device_url,
#         "executor":executor
#     }
class  AppDriver:
   def appDrvier(self, cps, executor):
    driver =  webdriver.Remote(desired_capabilities=cps, command_executor=executor)
    return driver
