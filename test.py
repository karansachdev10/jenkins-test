import unittest
from app import is_prime, fibonacci, factorial


class TestPrime(unittest.TestCase):
    def test_prime(self):
        #This function tests whether number is prime or not
        self.assertEqual(is_prime(2), True)


class TestFibonacci(unittest.TestCase):
    def test_fibo(self):
        #This function test whether result is equal to fibonacci
        self.assertEqual(fibonacci(10), 55)


class TestFactorial(unittest.TestCase):
    def test_fact(self):
        #This function tests whether result is equal to factorial
        self.assertEqual(factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
