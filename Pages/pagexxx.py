"""
@project:AppUIAuto
@author:lenovo
@file:pagexxx.py
@ide:PyCharm
@time:2019/6/10 16:50
@month:六月

"""
"""
每个页面的元素定位的方法
"""
from Helper.APPdriver import AppDriver
from Helper.appLocations import AppLocation
from Pages.login_location import username_location, password_location, login_location
from time import sleep


class Login:
    def __init__(self):
        dri = AppDriver
        self.driver = dri.driver()

    def input_userinfo(self, element_location, inputstring):
        sleep(5)
        self.driver.find_element_by_xpath(element_location).send_keys(inputstring)

    def login_button(self, element_location):
        sleep(5)
        self.driver.find_element_by_id(element_location).click()
