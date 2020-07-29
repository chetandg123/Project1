import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd


class download_clusterwise_csv():
    def __init__(self,driver):
        self.driver = driver
    def test_clusterwise(self):
        self.driver.find_element_by_xpath(Data.hyper).click()
        time.sleep(5)
        p =pwd()
        District_wise=Select(self.driver.find_element_by_id("downloader"))
        District_wise.select_by_visible_text(" Cluster_Wise Report ")
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(10)
        self.filename = p.get_download_dir() + "/Cluster_level_CRC_Report.csv"
        time.sleep(4)
        return os.path.isfile(self.filename)

    def remove_file(self):
        os.remove(self.filename)

