import unittest
from models import quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_quote = Quote('ALex',"I run like I can run")

    def test_instance(self):
        self.assertTrue(instance(self.new_quote,Quote))

if __name__ == '__main__':
    unittest.main()