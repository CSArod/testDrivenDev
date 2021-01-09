# write a program that prints numbers one to 100. But for multiples of three print "Fizz" instead of the number and for the multiples fo five print "Buzz". For the numbers 
# which are multiples of both three and five print fizz buzz.

import unittest #inports the unit test library
from fizz_buzz import fizz_buzz #import method from fizzbuzz.py

class Fizz_BuzzTestCase(unittest.TestCase):
    """Tests for `fizz_buzz.py.`"""


    def test_returns_a_list(self):
        """When you call fizzbuzz(), you should get a list back"""
        self.assertEqual(type(fizz_buzz()), list)
    
    def test_returns_list_of_100_elements(self):
        """ When you call fizz_buzz(), you should get a list of 100
        elements back"""
        self.assertEqual(len(fizz_buzz()), 100)

    def test_returns_the_correct_100_elements(self):
        """When you call fizzbuzz(), you should get the correct things back"""
        expected_output = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz","Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"]
        self.assertEqual(fizz_buzz(), expected_output)

if __name__ == '__main__':
    unittest.main()
