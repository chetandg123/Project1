import unittest
from selenium import webdriver

class Google(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/chetan/Downloads/chromedriver_linux64/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_launch(self):
        self.driver.get("http://google.com/")
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.page_source)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()