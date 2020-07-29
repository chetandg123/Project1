import csv
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from Data.parameters import Data
from Data.test_demo import Demo
from TS.arg import arg
from TS.reuse_func import cqube
from get_dir import pwd


class Blockdata_validation(unittest.TestCase):
    def setUp(self):
        # driver_path = pwd()
        # self.driver = webdriver.Chrome(driver_path.get_driver_path())
        p = pwd()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(p.get_driver_path(), chrome_options=options)
        # self.driver = webdriver.Chrome(os.path.abspath(os.curdir) + "Driver/chromedriver1", chrome_options=options)
        # driver = Demo(self.driver)
        # self.driver.get_headless()
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_student_report()
        time.sleep(5)
    def test_validate_schoolrecords(self):
        dist = self.driver.find_element_by_xpath(Data.SARD4).click()
        # blk =  self.driver.find_element_by_xpath(Data.SARB2).click()
        # time.sleep(5)
        # self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        lists =self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)-1
        print(count)
        self.assertNotEqual(0,count,msg="Block Does not contains Data")

    def tearDown(self,):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()