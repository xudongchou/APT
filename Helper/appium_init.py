"""
@project:AppUIAuto
@author:lenovo
@file:appium_init.py
@ide:PyCharm
@time:2019/7/18 17:44
@month:七月

"""
"""
appium webdriver 与手机端连接和断开链接的方法
"""
from client.android.stf_api.stf_api import StfDevice
import os,time
from Helper.helper import load_caps
from Conf.settings import AppDriver
from Conf.stf_conf import executer
from threading import Thread
threads =[]
class Appium_Init:
    def startup(self):
        self.remote_device = StfDevice()
        self.device_serial = self.remote_device.get_single_device()['serial']
        self.remote_device.rent_single_device(self.device_serial).text
        self.remote_connect_url = self.remote_device.get_user_device_remote_connect_url(self.device_serial)
        os.system("adb connect " + self.remote_connect_url)
        res = load_caps(self.device_serial)
        executor = executer
        self.driver = AppDriver.appDrvier(cps=res, executor=executor)

    def stop(self):
        self.driver.quit()
        os.system("adb disconnect " + self.remote_connect_url)
        self.remote_device.return_rented_device(self.device_serial).text
class Appium_Init_Group:
    def startup(self,instance):
        self.remote_devices = StfDevice()
        self.device_serials=self.remote_devices.get_all_device()
        for i in range(len(self.device_serials)):
            self.remote_connect_urls=self.remote_devices.get_user_device_remote_connect_url(self.device_serials[i])
            os.system("adb connect " + self.remote_connect_urls[i])
            time.sleep(30)
            res=load_caps(self.device_serials[i])
            executer = 'http://localhost:'+str(4723+2*i)+'/wd/hub'
            self.driver = AppDriver.appDrvier(cps=res,executer=executer)
            time.sleep(30)
            return self.driver



        # self.device_serial = self.remote_device.get_single_device()['serial']
        # self.remote_device.rent_single_device(self.device_serial).text
        # self.remote_connect_url = self.remote_device.get_user_device_remote_connect_url(self.device_serial)
        # os.system("adb connect " + self.remote_connect_url)
        # res = load_caps(self.device_serial)

        # executor = executer
        # self.driver = AppDriver.appDrvier(cps=res, executor=executor)

    def stop(self):
        for i in range(len(self.device_serials)):
            self.driver.quit()
            os.system("adb disconnect " + self.remote_connect_urls[i])
            self.remote_device.return_rented_device(self.device_serials[i]).text
