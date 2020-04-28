import time

from selenium import webdriver
import unittest
import HTMLTestRunner

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
    def testPythonScript(self):

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # driver.get_screenshot_as_file("/home/chetan/PycharmProjects/Project1/TestReports/Screenshots/login1.png")
        self.driver.get("http://www.github.com/")
        self.driver.find_element_by_xpath("//a[@href='/login']").click()
        time.sleep(5)
        self.driver.find_element_by_id("login_field").send_keys("chetandg143@gmail.com")
        self.driver.find_element_by_id("password").send_keys("3sl14cs009")
        self.driver.find_element_by_name("commit").click()
        time.sleep(5)

        self.driver.get_screenshot_as_file("/home/chetan/PycharmProjects/Project1/TestReports/Screenshots/login2.png")
        print(self.driver.title)
        self.driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']").click()

        print("execution ends")
        print(self.driver.title)
        assert  self.driver.title , "facebook logout!"
    # def testPythonFailScript(self):
    #     driver=self.driver
    #     driver.find_element_by_name("notExist").send_keys("done")

    def tearDown(self):

        self.driver.quit();


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="/home/chetan/PycharmProjects/Project1/TestReports/Reports/aa.html"))