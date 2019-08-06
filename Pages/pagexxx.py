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


def input_userinfo(inputstring):
    dri = AppDriver
    driver = AppDriver.driver()
    driver.find_element_by_xpath()
