import validate_otp as otp
import pytest
import unittest
from validate_otp import *


class TestProgramFunctions(unittest.TestCase):

    def test_validateEmail(self):

        result = validateEmail("shreyasdeshingkar@gmail.com")
        expected = True
        self.assertEqual(result, expected)

        result = validateEmail("manisha.deshingkar@gmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_generateOTP(self):
        otp = generateOTP()
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())


if __name__ == '__main__':
    pytest.main()
