from HTMLTestRunner import HTMLTestRunner
import unittest



class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Sanity_test = unittest.TestSuite()
        Sanity_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Block_Button_click.Blockbtn_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Block_details.test_blockdetails),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_CRCreport.test_crc),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_SR.test_SR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_TAR.test_TAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_Button_click.test_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_details.test_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dashboard_click.test_Dashboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_blk_cluster_select.Test_Distbllk),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_Block_select.Test_Distbllk),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_choose.Dist_choose),
            unittest.defaultTestLoader.loadTestsFromTestCase(Download_click.test_download),
            unittest.defaultTestLoader.loadTestsFromTestCase(Home_icon_click.test_homeicon),


            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_Btn_click.school_btn),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_details.school_details),
            unittest.defaultTestLoader.loadTestsFromTestCase(Url_test.url_test),
        ])
        # report = pwd()
        outfile = open("/home/chetan/cQube-New/Reports/sanity_Report.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Sanity Test Result '

        )

        runner1.run(Sanity_test)

if __name__ == '__main__':
    unittest.main()