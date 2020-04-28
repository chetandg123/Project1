import unittest

from HTMLTestRunner import HTMLTestRunner
from StringIO import StringIO


class Test_HTMLTestRunner(unittest.TestCase):

    def test0(self):
        self.suite = unittest.TestSuite()
        buf = StringIO.StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(buf)
        runner.run(self.suite)
        # didn't blow up? ok.
        self.assert_('</html>' in buf.getvalue())

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTest0),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTest1),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestBasic),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestHTML),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestLatin1),
            unittest.defaultTestLoader.loadTestsFromTestCase(SampleTestUnicode),
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf)       #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='<Demo Test>',
                    description='This demonstrates the report output by HTMLTestRunner.'
                    )
        runner.run(self.suite)