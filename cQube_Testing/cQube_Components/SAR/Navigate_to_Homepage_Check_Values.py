import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Home_page(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()
        time.sleep(5)
    def test_values(self):
        driver = cqube(self.driver)
        driver.navigate_to_student_report()


    def tearDown(self):
        time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
