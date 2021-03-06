
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class blockbtn_click(unittest.TestCase):
    def setUp(self):
        dri = pwd()


    def test_blockbtn(self):
        self.driver.find_element_by_xpath(Data.Blocks).click()
        time.sleep(10)
        driver = cqube(self.driver)
        driver.Details_text()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

