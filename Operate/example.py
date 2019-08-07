"""
@project:AppUIAuto
@author:lenovo
@file:example.py
@ide:PyCharm
@time:2019/6/10 16:50
@month:六月

"""
"""
每个page里面包含的业务的实现逻辑方法
"""
import unittest
from Pages.pagexxx import Login
from Pages.login_location import username_location, password_location, login_location


class Testlogin(unittest.TestCase):
    def test_login(self):
        l = Login()
        l.input_userinfo(username_location)
        l.input_userinfo(password_location)
        l.login_button(login_location)
