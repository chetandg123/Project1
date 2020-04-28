import unittest

from selenium import webdriver
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

class Amazon(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_app(self):
        self.driver.get("http://www.amazon.com/")
        print(self.driver.title)
        self.driver.get_screenshot_as_file("/home/chetan/PycharmProjects/Project1/TestReports/amazon.png")
        # self.driver.find_element_by_xpath("//input[@id='email']").send_keys("chetandg143@gmail.com")
        # self.driver.find_element_by_xpath("//input[@id='pass']").send_keys("9986809524")
        # self.driver.find_element_by_xpath("//input[@id='u_0_b']").click()
        # time.sleep(2)

    def test_title(self):
        print(self.driver.title)
        self.driver.forward()
        # assert  self.driver.title == "Facebook – log in or sign up"
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()