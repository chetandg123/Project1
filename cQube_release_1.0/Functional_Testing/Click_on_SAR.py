import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Click_on_SAR(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_menu(self):
        driver = cqube(self.driver)
        driver.navigate_to_student_report()
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.logout).click()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()