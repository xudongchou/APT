"""
@project:AppUIAuto
@author:lenovo
@file:test_xxx.py
@ide:PyCharm
@time:2019/6/10 16:51
@month:六月

"""

from client.android.stf_api.stf_api import StfDevice
from unittest import TestCase
from Helper.appium_init import Appium_Init


class CreditEaseAgent(TestCase):
    def setUp(self):
       self.driver= Appium_Init.startup()


    def tearDown(self):
        Appium_Init.stop()

    def test_zxbx(self):
        pass
