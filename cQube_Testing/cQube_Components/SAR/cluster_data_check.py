
import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.arg import arg
from TS.reuse_func import cqube
from get_dir import pwd


class dist_test(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()
        driver.navigate_to_student_report()
        time.sleep(5)
    def test_checking_dots_on_cluster(self):
        dist = self.driver.find_element_by_xpath(Data.SARD3).click()
        blk = self.driver.find_element_by_xpath(Data.SARB1).click()
        clu = self.driver.find_element_by_xpath(Data.SARC1).click()

        time.sleep(5)
        lists = self.driver.find_elements_by_class_name(Data.dots)
        count = len(lists)
        self.assertNotEqual(0,count,msg="Dots are not Present on map")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()