from selenium import webdriver
import unittest


class NewCustomerTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_purchase_shoes_and_save_details_for_next_time(self):
        # Derek googles best cross country shoes and finds Shoepersonic 
        # He clicks on the link to open the home page.
        self.browser.get('http://localhost:8000')

        # He sees he has come to the right place as the title in the browser
        # says running shoes
        self.assertIn('django', self.browser.title)
        self.fail("Finish the test")

        # He clicks the shop now button

        # He is brought to a list of all the shoes

        # He browses the shoes and spots one he likes the look of and clicks to view details

        # He is sold, and adds the shoe to his basket

        # He then goes to the first checkout

        # He enters his email address and running club if he wants and clicks next

        # He adds in his delivery details and clicks next

        # He adds his card details and places an order

        # He is shown a celebration screen with his order number

        # He adds his details to save them for next time and is excited for his new shoes
    
if __name__ == '__main__':
    unittest.main()


