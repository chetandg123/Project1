import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Click_on_pwd(unittest.TestCase):
    def setUp(self):
        path_exe = pwd()
        self.driver = webdriver.Chrome(path_exe.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_passwordchange()
        time.sleep(3)
    def test_changepassword(self):
        self.driver.find_element_by_id(Data.p_change).click()
        pwd =self.driver.find_element_by_xpath("//h2").text
        self.assertEqual(pwd,"Change Password","Change password is not found!..")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

if __name__ == "__main__":
        unittest.main()