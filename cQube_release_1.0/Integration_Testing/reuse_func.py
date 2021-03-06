import os
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Data.parameters import Data


class cqube():

    def __init__(self, driver):
        self.driver = driver

    def open_cqube_appln(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(Data.url)

    def login_cqube(self):
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def navigate_to_student_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.year).click()
        self.driver.find_element_by_xpath(Data.august).click()

    def navigate_to_student_report_S(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.year).click()
        self.driver.find_element_by_xpath(Data.Sept).click()

    def navigate_to_student_report_O(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()
        self.driver.find_element_by_xpath(Data.year).click()
        self.driver.find_element_by_xpath(Data.Oct).click()


    def navigate_to_semester_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SR).click()

    def navigate_to_crc_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.crc).click()

    def select_month_year(self,y,m):
        year = Select(self.driver.find_element_by_name(Data.select_year))
        month = Select(self.driver.find_element_by_name(Data.select_month))
        time.sleep(2)
        year.select_by_visible_text(y)
        time.sleep(2)
        month.select_by_visible_text(m)
        time.sleep(2)

    def Details_text(self):
        Details = self.driver.find_elements_by_xpath(Data.details)
        time.sleep(5)
        for i in range(len(Details)):
           print(Details[i].text)

    def Click_HomeButton(self):
            self.driver.find_element_by_id(Data.Home_icon).click()
            time.sleep(3)

    def CRC_footers(self):
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)

    def test_Distnames(self):
        dnames = self.driver.find_elements_by_xpath(Data.Dnames)
        for i in range(len(dnames)):
            print(dnames[i].text)
            time.sleep(2)

    def dots_dist(self):
        distnames = self.driver.find_elements_by_xpath(Data.Dnames)
        for i in range(len(distnames)):
            print(distnames[i].click())
            time.sleep(3)
            lists = self.driver.find_elements_by_class_name(Data.dots)
            time.sleep(2)
            count = len(lists) - 1
            print(distnames[i].text, ":", count)

    def X_Yaxis(self):
        x_axis = self.driver.find_elements_by_xpath(Data.xaxis)
        time.sleep(2)
        print("X axis menu list...")
        for i in range(len(x_axis)):
            print(x_axis[i].text)
        print("Y axis menu list...")
        time.sleep(2)
        y_axis = self.driver.find_elements_by_xpath(Data.yaxis)
        for i in range(len(y_axis)):
            print(y_axis[i].text)

    def crcDist_click(self):
        clu = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(clu)):
            clu[i].click()
            time.sleep(6)

    def clusters_text(self):
        cluster = self.driver.find_elements_by_xpath(Data.clusterlist)
        for i in range(len(cluster)):
            cluster[i].click()
            print(cluster[i].text)
            time.sleep(5)

    def X_axis(self):
        xvalues = self.driver.find_elements_by_xpath(Data.xaxis)
        for i in range(len(xvalues)):
            xvalues[i].click()
            time.sleep(3)

    def get_driver_path(self):
        os.chdir('../')
        executable_path = os.path.join(os.getcwd(), 'Driver/chromedriver1')
        return executable_path

    def crc_validation(self):
        self.driver.find_element_by_xpath("//*[@id='select']/select/option[2]").click()
        print(self.driver.find_element_by_xpath("//*[@id='select']/select/option[2]").text)
        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@id='select']/select/option[3]").click()
        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@id='select']/select/option[4]").click()
        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@id='select']/select/option[5]").click()
        time.sleep(5)

    #SAR_2
    def blocks_names(self):
        self.driver.find_element_by_xpath(Data.Blocks).click()
        time.sleep(15)
        print("Block details..")
        infob = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infob)):
            print(infob[i].text)

    def clusters_names(self):
        self.driver.find_element_by_xpath(Data.Clusters).click()
        time.sleep(15)
        print("Cluster details..")
        infoc = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infoc)):
            print(infoc[i].text)

    def schools_test(self):
        self.driver.find_element_by_xpath(Data.Schools).click()
        print("for schools details...")
        time.sleep(15)
        infos = self.driver.find_elements_by_xpath(Data.details)
        for i in range(len(infos)):
            print(infos[i].text)

    def Total_details(self):
        details = self.driver.find_elements_by_xpath(Data.SAR_Details)
        for i in range(len(details)):
            print(details[i].text)
            time.sleep(3)

    def test_mouse_over(self):
            lists = self.driver.find_elements_by_class_name(Data.dots)

            def mouseover(i):
                action = ActionChains(self.driver)
                action.move_to_element(lists[i]).perform()
                time.sleep(3)
                del action

            i = 0
            while i < len(lists):
                mouseover(i)
                i = i + 1

    def Table_data(self):
        tabledata = self.driver.find_elements_by_xpath(Data.distrows)
        for i in range(len(tabledata)):
            print(tabledata[i].text)
        footer = self.driver.find_elements_by_xpath(Data.footer)
        for i in range(len(footer)):
            print(footer[i].text)
            time.sleep(5)


    def x_yaxis(self):
        xaxis_lists = self.driver.find_elements_by_xpath(Data.xaxis)
        yaxis_lists = self.driver.find_elements_by_xpath(Data.yaxis)
        for i in range(len(xaxis_lists)):
            xaxis_lists[i].click()
            print(xaxis_lists[i].text)
            time.sleep(4)
            for j in range(len(yaxis_lists)):
                yaxis_lists[i].click()
                print(yaxis_lists[j].text)
                time.sleep(4)


