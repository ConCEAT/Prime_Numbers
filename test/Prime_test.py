import os
import sys
import unittest

sys.path.insert(0,os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
from source import Prime

class TestCheckIfPrime(unittest.TestCase):

    def test_primes(self):
        numbers = [2,3,5,11,19,101]
        for number in numbers:
            with self.subTest(case = number): 
                self.assertTrue(Prime.checkIfPrime(number))

    def test_nonPrimes(self):
        numbers = [1,4,6,25,1000,18]
        for number in numbers:
            with self.subTest(case = number):
                self.assertFalse(Prime.checkIfPrime(number))

    def test_values(self):
        numbers = [0,-1,-121]
        for number in numbers:
            with self.subTest(case = number):
                self.assertRaises(ValueError,Prime.checkIfPrime,number)
    
    def test_types(self):
        numbers = [1.4,'4','four',2+5j,0.0,True,[]]
        for number in numbers:
            with self.subTest(case = number):
                self.assertRaises(TypeError,Prime.checkIfPrime,number)


if __name__ == '__main__':
    unittest.main()