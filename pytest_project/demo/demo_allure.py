import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        self.launch_site()
        # self.verify_site()

    @pytest.allure.step("Launch site")
    def launch_site(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://google.com/")
        print(self.driver.current_url)

    # @pytest.allure.step("Verify Title loaded")
    # def verify_site(self):
    #     wait = WebDriverWait(self.driver, 5)
    #     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))