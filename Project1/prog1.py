import unittest
from time import time

from selenium import webdriver
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

class Facebook(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.get("http://www.facebook.com/")
        print(self.driver.title)
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("chetandg143@gmail.com")
        self.driver.find_element_by_xpath("//input[@id='pass']").send_keys("9986809524")
        self.driver.find_element_by_xpath("//input[@id='u_0_b']").click()
        # time.sleep(2)

    def test_asser(self):
        print(self.driver.title)
        # assert  self.driver.title == "Facebook – log in or sign up"
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()