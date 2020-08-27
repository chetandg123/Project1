import configparser
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Data.parameters import Data
from get_dir import pwd


class GetData():
    def __init__(self):
         self.p = pwd()

    def get_domain_name(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['domain']

    def get_username(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['username']

    def get_password(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['password']

    def get_jsonfile(self):
        config = configparser.ConfigParser()
        config.read(self.p.get_config_ini_path())
        return config['config']['json_file']

    def get_driver(self):
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.p.get_download_dir()}
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options, executable_path=self.p.get_driver_path())
        return self.driver

    def open_cqube_appln(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(self.get_domain_name())
        self.driver.implicitly_wait(60)

    def page_loading(self, driver):
        try:
            driver.implicitly_wait(5)
            self.driver = driver
            for x in range(1, 10):
                elem = self.driver.find_element_by_id('loader').text
                elem.encode('utf-8')
                if str(elem) == "Loading…":
                    time.sleep(1)
                if str(elem) != "Loading…":
                    time.sleep(1)
                    break
        except NoSuchElementException:
            pass

    def login_cqube(self, driver):
        self.driver = driver
        self.driver.find_element_by_id(Data.email).send_keys(self.get_username())
        self.driver.find_element_by_id(Data.passwd).send_keys(self.get_password())
        self.driver.find_element_by_id(Data.login).click()
        # i = input("Enter the otp :")
        # self.driver.find_element_by_id("otp").send_keys(i)
        # self.driver.find_element_by_id(Data.login).click()
        self.driver.find_element_by_xpath(Data.admin_console).click()


    def navigate_to_nifipage(self):
        self.driver.find_element_by_id("menu").click()
        self.page_loading(self.driver)
        self.driver.find_element_by_id("nifi").click()
        self.page_loading(self.driver)
