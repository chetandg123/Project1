import csv
import os
import re
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class download_report():
    def __init__(self,driver):
        self.driver = driver
    def test_schools(self):
        p = pwd()
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(3)
        District_wise = Select(self.driver.find_element_by_id("downloader"))
        time.sleep(2)
        District_wise.select_by_visible_text(" Dist_Wise Report ")
        time.sleep(5)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.filename = p.get_download_dir() + "/Dist_level_Infra_Report.csv"
        return os.path.isfile(self.filename)

    def remove_csv(self):
        os.remove(self.filename)
