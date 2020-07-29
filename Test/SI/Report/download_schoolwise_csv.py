import os
import time

from selenium.common import exceptions
from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class school_wise_donwload():
    def __init__(self,driver):
        self.driver = driver

    def test_schoolwise(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        try:
            p = pwd()
            District_wise=Select(self.driver.find_element_by_name("downloadType"))
            District_wise.select_by_index(4)
            time.sleep(5)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(30)
            self.filename = p.get_download_dir() + "/School_level_CRC_Report.csv"
            return os.path.isfile(self.filename)

        except exceptions.NoSuchElementException:
            print("school wise csv downloaded")

    def remove_csv(self):
        os.remove(self.filename)

