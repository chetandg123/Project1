import time
import unittest

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class nifi_schedular(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    def test_nifi_icon_in_landingpage(self):
        count = 0
        self.driver.find_element_by_xpath(Data.nifi_sc).click()
        self.data.page_loading(self.driver)
        if "nifi-shedular" in self.driver.current_url:
            print("Nifi schedular page is present ")
        else:
            print("Nifi schedular page is not exists ")
            count = count + 1
        self.assertEqual(0,count,msg="Nifi schedular page not exists")
        self.driver.find_element_by_id("homeBtn").click()

    def test_dashboard_nifi(self):
        count = 0
        self.data.navigate_to_nifipage()
        self.driver.find_element_by_id("homeBtn").click()
        if "home" in self.driver.current_url:
            print("Navigated back to Home page")
        else:
            print("Landing page is not exist ")
            count = count + 1
        self.assertEqual(0,count,msg="homebtn is not working")

    def test_tableorder(self):
        self.data.navigate_to_nifipage()
        self.driver.find_element_by_xpath(Data.t_head).click()
        self.data.page_loading(self.driver)
        values = self.driver.find_elements_by_xpath("//th[1]")
        for i in values:
            print(i.get_attribute("aria-sort"))
        self.data.page_loading(self.driver)
        self.driver.find_element_by_xpath(Data.t_head).click()
        self.data.page_loading(self.driver)
        value = self.driver.find_elements_by_xpath("//th[1]")
        for i in value:
            print(i.get_attribute("aria-sort"))
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id("homeBtn").click()

    def test_search_box(self):
        self.data.navigate_to_nifipage()
        self.driver.find_element_by_xpath("//input[@type='search']").send_keys("cr")
        # self.driver.find_element_by_xpath(').get_attribute('value')
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()

    def test_schedule_time(self):
        self.data.navigate_to_nifipage()
        tset = Select(self.driver.find_element_by_id('role'))
        for i in range(1,len(tset.options)):
            tset.select_by_index(i)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()


    def test_stoppinghours(self):
        self.data.navigate_to_nifipage()
        tset = Select(self.driver.find_element_by_id('role'))
        for i in range(1, len(tset.options)):
            tset.select_by_index(i)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()

    def test_nifi_process_sceduling(self):
        self.data.page_loading(self.driver)
        self.data.navigate_to_nifipage()
        tset = Select(self.driver.find_element_by_id('role'))
        tset.select_by_index(3)
        self.data.page_loading(self.driver)
        tset = Select(self.driver.find_element_by_id('role'))
        tset.select_by_index(5)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('schedule').click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('homeBtn').click()


    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()

