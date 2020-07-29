import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.arg import arg
from TS.reuse_func import cqube
from get_dir import pwd


class Sel_type(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()
        driver.navigate_to_student_report()
        time.sleep(5)
    def test_select(self):
        self.driver.find_element_by_id(Data.SAR_Schools_btn).click()
        time.sleep(15)
        self.driver.find_element_by_xpath(Data.Home_icon).click()
        print(self.driver.title, " : ",self.driver.current_url)
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()