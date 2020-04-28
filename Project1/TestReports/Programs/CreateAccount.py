from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
class CreateAccount(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        driver.implicitly_wait(10)
        driver.get("http://www.copy.com")
        driver.maximize_window()

    def test_main(self):
        createNewAccount = driver.find_element_by_xpath("/html/body/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/form/div[5]/div[1]/a")
        createNewAccount.click()

        firstName = driver.find_element_by_xpath("//*[@id='dom_id_3']")
        lastName = driver.find_element_by_xpath("//*[@id='dom_id_4']")
        emailField = driver.find_element_by_xpath("//*[@id='dom_id_5']")
        passwordField = driver.find_element_by_xpath("//*[@id='dom_id_6']")

        submitButton = driver.find_element_by_xpath("/html/body/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/form/button")

        firstName.send_keys("mike")
        lastName.send_keys("mano")
        emailField.send_keys("money@qa.test")
        passwordField.send_keys("test12")

        submitButton.click()

    try:
         xpath = driver.find_element_by_xpath("/html/body/main/div/article[2]/div[4]/header/div[2]/div/div[4]/a")
         print("Yeah")

    except NoSuchElementException: print("Failed")
    raise Exception(NoSuchElementException)
    # for i in range(100):
    #     email_address = "money" + str(i) + "@qa.test"
    #     firstName.send_keys("mike")
    #     lastName.send_keys("mano")
    #     emailField.send_keys(email_address)
    #     passwordField.send_keys("test12")
    #     submitButton.click()

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()

