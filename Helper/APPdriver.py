"""
@project:APT
@author:lenovo
@file:APPdriver.py
@ide:PyCharm
@time:2019/8/6 15:25
@month:八月

"""
from client.android.stf_api.stf_api import StfDevice
import os, time
from Helper.helper import load_caps
from Conf.settings import AppDriver
from Conf.stf_conf import executer


class AppDriver:
    def driver(self):
        remote_device = StfDevice()
        device_serial = remote_device.get_single_device()['serial']
        remote_device.rent_single_device(device_serial).text
        remote_connect_url = remote_device.get_user_device_remote_connect_url(device_serial)
        os.system("adb connect " + remote_connect_url)
        res = load_caps(device_serial)
        executor = executer
        driver = AppDriver.appDrvier(cps=res, executor=executor)
        return driver
