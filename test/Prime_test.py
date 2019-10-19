import unittest
import sys
sys.path.append('..')
from PrimeNumbers.source.Prime import checkIfPrime

class TestCheckIfPrime(unittest.TestCase):

    def test_primes(self):
        numbers = [2,3,5,11,19,101]
        for number in numbers:
            with self.subTest(number = number): 
                self.assertTrue(checkIfPrime(number))


if __name__ == '__main__':
    unittest.main()