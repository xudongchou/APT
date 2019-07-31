"""
@project:AppUIAuto
@author:lenovo
@file:settings.py
@ide:PyCharm
@time:2019/6/10 16:49
@month:六月

"""
import os
from appium import webdriver

# ANDROID_BASE_CAPS = {
#     'app': os.path.abspath('../apps/ApiDemos-debug.apk'),
#     'automationName': 'UIAutomator2',
#     'platformName': 'Android',
#     'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION') or '8.0',
#     'deviceName': os.getenv('ANDROID_DEVICE_VERSION') or 'Android Emulator',
#     'packageName': '',
#     'activityName': '',
#     'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}  # 小程序需要添加
# }
#
# IOS_BASE_CAPS = {
#     'app': os.path.abspath('../apps/TestApp.app.zip'),
#     'automationName': 'xcuitest',
#     'platformName': 'iOS',
#     'platformVersion': os.getenv('IOS_PLATFORM_VERSION') or '12.2',
#     'deviceName': os.getenv('IOS_DEVICE_NAME') or 'iPhone 8 Simulator',
#     # 'showIOSLog': False,
#     'uuid': '',
#     'xcodeOrgId': '',
#     'xcodeSigningId':'iPhone Developer',
#
# }
# EXECUTOR = 'http://127.0.0.1:4723/wd/hub'
class  AppDriver(object):
   def appDrvier(self, cps, executor):
    driver =  webdriver.Remote(desired_capabilities=cps, command_executor=executor)
    return driver