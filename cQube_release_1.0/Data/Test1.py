#


import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd
from selenium.webdriver.support import expected_conditions as EC


class blocks(unittest.TestCase):
    def setUp(self):
        p = pwd()
        self.driver = webdriver.Chrome(p.get_driver_path())
        self.driver.get("https://cqube.tibilprojects.com")
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("exampleInputEmail").send_keys("srinivas@cqube.com")
        self.driver.find_element_by_id("exampleInputPassword").send_keys("tibil123")
        self.driver.find_element_by_id("login").click()
        time.sleep(5)

    def test_blockbtn(self):
        self.driver.implicitly_wait(50)
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.element_to_be_clickable((By.ID, 'block')))
        element.click()
        # time.sleep(3)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        count = len(dots) - 1
        print(count)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

# import time
#
# print("Start : %s" % time.ctime())
# time.sleep(5)
# print("End : %s" % time.ctime())
#

