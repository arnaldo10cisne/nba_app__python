import unittest
from nba_module import *


class testNbaModule(unittest.TestCase):

    #Tests for the ORDER_ARRAY function
    def test_order_array(self):
        obj = [{"h_in":0},{"h_in":2},{"h_in":4},{"h_in":6},{"h_in":8},{"h_in":1},{"h_in":3},{"h_in":5},{"h_in":7},{"h_in":9}]
        self.assertEqual(order_array(obj), [{"h_in":0},{"h_in":1},{"h_in":2},{"h_in":3},{"h_in":4},{"h_in":5},{"h_in":6},{"h_in":7},{"h_in":8},{"h_in":9}])
        self.assertEqual(order_array([{"h_in":5},{"h_in":6}]), [{"h_in":5},{"h_in":6}])
        self.assertEqual(order_array([{"h_in":6}]), [{"h_in":6}])
        self.assertEqual(order_array([{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":5},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6}]), [{"h_in":5},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6}])
        self.assertEqual(order_array([{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":7},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6}]), [{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":6},{"h_in":7}])
        self.assertEqual(order_array([]), [])
        with self.assertRaises(TypeError):
            order_array([3,5,7,1])


    #Tests for the VALIDATE_USER_INPUT function
    def test_validate_user_input(self):
        self.assertEqual(validate_user_input(5,3,7), "Valid")
        self.assertEqual(validate_user_input(5,5,7), "Valid")
        self.assertEqual(validate_user_input(5,3,5), "Valid")
        self.assertNotEqual(validate_user_input(1,3,5), "Valid")
        self.assertNotEqual(validate_user_input(7,3,5), "Valid")
        self.assertEqual(validate_user_input(-2,3,5), "Please enter a positive integer bigger than zero")
        self.assertEqual(validate_user_input(0,0,5), "Please enter a positive integer bigger than zero")


    #Tests for the SEARCH_FIRST_RESULT function
    def test_search_first_result(self):
        obj = [{"h_in":0},{"h_in":1},{"h_in":2},{"h_in":3},{"h_in":4},{"h_in":5},{"h_in":6},{"h_in":7},{"h_in":8},{"h_in":9}]
        self.assertEqual(search_first_result(obj, 0, len(obj), 0), 0)
        self.assertEqual(search_first_result(obj, 0, len(obj), 6), 6)
        self.assertEqual(search_first_result(obj, 0, len(obj), 9), 9)
        self.assertEqual(search_first_result([{"h_in":6}], 0, len([{"h_in":6}]), 6), 0)
        self.assertEqual(search_first_result([], 0, len([]), 5), None)


if __name__ == '__main__':
    unittest.main()