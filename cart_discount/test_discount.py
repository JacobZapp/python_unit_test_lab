import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):


    def test_list_of_one_price(self):

        # Arranging a test scenario
        prices = [10]
        expected_discount = 0

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_of_three_prices(self):

        # Arranging a test scenario
        prices = [10, 4, 20]
        expected_discount = 4

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    # TODO more unit tests here. Each test should test one scenario

    # Happy path - 4 things in the list, one of them is the cheapest
    def test_list_of_four_prices(self):

        # Arranging a test scenario
        prices = [15, 200, 10, 100]
        expected_discount = 10

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    # happy path 2 - 2 things in the list
    def test_list_of_two_prices(self):

        # Arranging a test scenario
        prices = [100, 3]
        expected_discount = 0

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    # unhappy path - empty list
    def test_empty_list(self):

        # Arranging a test scenario
        prices = []
        expected_discount = 0

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    # happy path 3 - 3 things in the list, all the same price
    def test_list_of_three_prices_all_same(self):

        # Arranging a test scenario
        prices = [10, 10, 10]
        expected_discount = 10

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    # unhappy path - list of negative numbers
    def test_list_of_negative_numbers(self):

        # Arranging a test scenario
        prices = [-10, -20, -30]
        expected_discount = -30

        # Action - do the thing you want to test
        function_returned_discount = discount(prices)

        # Assert - check that the thing you expected to happen, did happen
        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_very_large_numbers(self):

        # Arranging
        prices = [1000000000000000000000000000000000000, 200000000000000000000000000000000000, 3000000000000000000000000000000000000000000000000000000]
        expected_discount = 200000000000000000000000000000000000

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_of_floats(self):

        # Arranging
        prices = [10.99, 5.99, 20.99]
        expected_discount = 5.99

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

        # zeros
    def test_list_of_zeros(self):

        # Arranging
        prices = [0, 0, 0]
        expected_discount = 0

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_with_zero_and_positive_numbers(self):

        # Arranging
        prices = [0, 10, 20]
        expected_discount = 0

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_with_mixed_numbers(self):

        # Arranging
        prices = [1.2, 5, 10]
        expected_discount = 1.2

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)
    
    def test_with_one_negative_number(self):

        # Arranging
        prices = [10, -5, 20]
        expected_discount = -5

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_mixed_numbers_and_zero(self):

        # Arranging
        prices = [0, -5, 10]
        expected_discount = -5

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)
    
    def test_with_multiple_smallest_numbers(self):

        # Arranging
        prices = [10, 5, 5, 20]
        expected_discount = 5

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_all_negative_numbers(self):

        # Arranging
        prices = [-10, -20, -30]
        expected_discount = -30

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_with_large_negative_numbers(self):

        # Arranging
        prices = [-1000000000000000000, -2000000000000, -3000000]
        expected_discount = -1000000000000000000

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_large_numbers_but_not_enough_items(self):

        # Arranging
        prices = [1000000000000000000, 2000000000000]
        expected_discount = 0

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_discount_non_numeric(self):
        prices = [10, "hello", 5]
        with self.assertRaises(TypeError):
         discount(prices)

    def test_list_of_all_strings(self):
        prices = ["10", "5", "20"]
        
        expected_discount = '10'

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_with_none(self):
        prices = [10, None, 5]
        with self.assertRaises(TypeError):
            discount(prices)

    def test_list_of_strings_but_not_enough_items(self):
        prices = ["10", "5"]
        expected_discount = 0

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_list_none(self):
        prices = None
        with self.assertRaises(TypeError):
            discount(prices)

    def test_string_instead_of_list(self):
        prices = "Testing String"
       
        expected_discount = ' '

        function_returned_discount = discount(prices)

        self.assertEqual(expected_discount, function_returned_discount)

    def test_dictionary_instead_of_list(self):
        prices = {"item1": 10, "item2": 5, "item3": 20}
        
        expected_discount = 'item1'

        function_returned_discount = discount(prices)
        self.assertEqual(expected_discount, function_returned_discount)

if __name__ == '__main__':
    unittest.main()