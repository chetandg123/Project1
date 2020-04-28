

import unittest

import os


from HTMLTestRunner import HTMLTestRunner

from prog1 import Facebook


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Facebook.prog1),
            # unittest.defaultTestLoader.loadTestsFromTestCase(),
            # unittest.defaultTestLoader.loadTestsFromTestCase(myfacebook.facebook),
        ])

        outfile = open("Prog1.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'

        )

        runner1.run(smoke_test)

if __name__ == '__main__':
    unittest.main()