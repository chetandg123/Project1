

import unittest
from TestReports.Programs import fb, amazon
from TestReports.Programs import google
from TestReports.Programs import Logintest
# from package name import class name
from HTMLTestRunner import HTMLTestRunner

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            # #  program name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(fb.Facebook),
            unittest.defaultTestLoader.loadTestsFromTestCase(amazon.Amazon),
            unittest.defaultTestLoader.loadTestsFromTestCase(google.Google),
            unittest.defaultTestLoader.loadTestsFromTestCase(Logintest.LoginTest)
        ])

        outfile = open("/home/chetan/PycharmProjects/Project1/TestReports/Reports/4.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description=' Test Report '

        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()