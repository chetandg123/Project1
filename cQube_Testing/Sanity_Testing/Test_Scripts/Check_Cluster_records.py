import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Test_Distbllk(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(executable_path=driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()
        driver.navigate_to_student_report()

    def test_url(self):
        self.driver.find_element_by_xpath(Data.SARD17).click()
        self.driver.find_element_by_xpath(Data.SARB3).click()
        self.driver.find_element_by_xpath(Data.SARC2).click()
        time.sleep(5)
        dots = self.driver.find_elements_by_xpath(Data.dots)
        count = len(dots)
        self.assertEqual(0,count,msg="Failed ")
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()