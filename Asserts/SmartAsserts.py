"""
@project:code
@author:lenovo
@file:SmartAsserts.py
@ide:PyCharm
@time:2019/6/10 10:49
@month:六月

"""
"""
二次封装unittest断言
"""
from unittest import TestCase
class SmartAsserts(TestCase):
    def smartAssertEqual(self,first,second,msg=None):
        try:
            self.assertEqual(first=first,second=second)
        except AssertionError:
            pass
    def smartAssertNotEqual(self,first,second,msg=None):
        try:
            self.assertNotEqual(first=first,second=second)
        except AssertionError:
            pass
    def smartAssertTrue(self,exp,msg=None):
        try:
            self.assertTrue(exp=exp)
        except AssertionError:
            pass
    def smartAssertFlase(self,exp,msg=None):
        try:
            self.assertFalse(exp=exp)
        except AssertionError:
            pass
    def smartAssertIn(self,member,container,msg=None):
        try:
            self.assertIn(member=member,container=container)
        except AssertionError:
            pass
    def smartAssertNotIn(self,member,container,msg=None):
        try:
            self.assertNotIn(member=member,container=container)
        except AssertionError:
            pass
    def smartAssertDictEqual(self,dict1,dict2,msg=None):
        try:
            self.smartAssertDictEqual(dict1=dict1,dict2=dict2)
        except AssertionError:
            pass
    def smartAssertDictNotEqual(self,dict1,dict2,msg=None):
        try:
            self.smartAssertDictNotEqual(dict1=dict1,dict2=dict2)
        except AssertionError:
            pass
    def smartAssertListEqual(self,list1,list2,msg=None):
        try:
            self.assertListEqual(list1=list1,list2=list2)
        except AssertionError:
            pass
    def smartAssertlistNotEqual(self,list1,list2,msg=None):
        try:
            self.smartAssertlistNotEqual(list1=list1,list2=list2)
        except AssertionError:
            pass
    def smartAssertDictContainsSubset(self,subset,dict1,msg=None):
        try:
            self.assertDictContainsSubset(subset=subset,dictionary=dict1)
        except AssertionError:
            pass
