import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data


class check_home():
    def __init__(self,driver):
        self.driver = driver
    def test_home(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        dist = Select(self.driver.find_element_by_name("myDistrict"))
        dist.select_by_index(1)
        time.sleep(5)
        block = Select(self.driver.find_element_by_name("myBlock"))
        block.select_by_index(1)
        time.sleep(5)
        cluster = Select(self.driver.find_element_by_name("myCluster"))
        cluster.select_by_index(1)
        time.sleep(5)
        self.driver.find_element_by_id(Data.homeicon).click()
        time.sleep(5)

