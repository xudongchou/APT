"""
@project:AppUIAuto
@author:lenovo
@file:appLocations.py
@ide:PyCharm
@time:2019/6/11 14:07
@month:六月

"""
"""
app端常用的定位方法
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.location import Location
from Conf.settings import ANDROID_BASE_CAPS,IOS_BASE_CAPS,EXECUTOR
from Conf.settings import AppDriver
from time import sleep
import os
from datetime import datetime
from appium.webdriver.mobilecommand import MobileCommand
from Helper.Logs import logger
from Helper.APPdriver import AppDriver
class AppLocation(object):
    def __init__(self,driver=None):
        self.driver = driver
    def android_spiner(self, xpath1, xpath2, inputstring):
        driver = self.driver
        spiner = driver.find_element_by_xpath(xpath1)
        spiner.click()
        driver.scroll(inputstring)
        label=driver.find_element_by_xpath(xpath2)
        label.click()

    def seekBar(self, xpath):
        driver = self.driver
        slider = driver.find_element_by_xpath(xpath)
        location = slider.location
        location_x = location['x']
        location_y = location['y']
        location_x_end = location_x + slider.size['width']
        location_y_end = location_y + slider.size['height']
        touch_action = TouchAction(driver)
        touch_action.tap(location_x, location_y).wait(1000).move_to(location_x_end, location_y_end).release().perform()
    def webEdit(self,xpath,inputstring):
        driver = self.driver
        webedit = driver.find_element_by_xpath(xpath=xpath)
        sleep(1)
        webedit.send_keys(inputstring)

    def save_Screen(self):
        driver = self.driver
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        datime = datetime.now()
        screen_time = datime.strftime(datime,"%Y-%m-%d_%H:%M:%S")
        screen_file = base_path + '\\ScreenShot\\'
        driver.save_screenshot(screen_file+screen_time+'.png')

    """
    @default_context:local context
    @switch_context:the context will be switched
    """

    def switch_To_context(self, default_context, switch_context):
        driver = self.driver
        contexts = driver.context()
        if default_context in contexts and switch_context in contexts:
            driver.execute(MobileCommand.SWITCH_TO_CONTEXT({"name": switch_context}))
            current_context = driver.current_context()
            if current_context == switch_context:
                logger.info('切换成功')
            else:
                logger.info('切换失败')
        else:
            logger.info('存在的context少于2个，无法进行切换')
        driver.find_element_by_ios_predicate()

    def ios_predicate(self, predicate_string):
        driver = self.driver
        driver.find_element_by_ios_predicate(predicate_string)

    def ios_chain(self, chain_string):
        driver = self.driver
        driver.find_elements_by_ios_class_chain(chain_string)

    def ios_uiautomation(self, uia_string):
        driver = self.driver
        driver.find_element_by_ios_uiautomation(uia_string)

    def android_viewtag(self, tag):
        driver = self.driver
        driver.find_element_by_android_viewtag(tag)

    def android_uiautomator(self, uia_string):
        driver = self.driver
        driver.find_element_by_android_uiautomator(uia_string)
