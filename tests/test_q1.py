"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q1 import validate_password

class TestValidatePassword(unittest.TestCase):
    
    def test_valid_password(self):
        """Test a password that meets all requirements"""
        result = validate_password("Password123!")
        self.assertTrue(result)
    
    def test_valid_password_with_all_special_chars(self):
        """Test valid passwords with different special characters"""
        valid_passwords = [
            "Password1!",
            "Password1@",
            "Password1#",
            "Password1$",
            "Password1%",
            "Password1^",
            "Password1&",
            "Password1*"
        ]
        for pwd in valid_passwords:
            result = validate_password(pwd)
            self.assertTrue(result)
    
    def test_password_too_short(self):
        """Test password that is too short"""
        result = validate_password("Pass1!")
        self.assertFalse(result)
    
    def test_password_no_uppercase(self):
        """Test password without uppercase letter"""
        result = validate_password("password123!")
        self.assertFalse(result)
    
    def test_password_no_lowercase(self):
        """Test password without lowercase letter"""
        result = validate_password("PASSWORD123!")
        self.assertFalse(result)
    
    def test_password_no_digit(self):
        """Test password without a digit"""
        result = validate_password("Password!@#")
        self.assertFalse(result)
    
    def test_password_no_special_char(self):
        """Test password without special character"""
        result = validate_password("Password123")
        self.assertFalse(result)
    
    def test_password_multiple_failures(self):
        """Test password that fails multiple requirements"""
        result = validate_password("pass")
        self.assertFalse(result)
    
    def test_password_exactly_8_chars(self):
        """Test password with exactly 8 characters (boundary)"""
        result = validate_password("Pass123!")
        self.assertTrue(result)
    
    def test_empty_password(self):
        """Test empty password"""
        result = validate_password("")
        self.assertFalse(result)
    
    def test_long_valid_password(self):
        """Test a long password that meets all requirements"""
        result = validate_password("ThisIsAVeryLongPassword123!")
        self.assertTrue(result)
    
    def test_password_with_invalid_special_char(self):
        """Test password with special char not in the allowed list"""
        result = validate_password("Password123-")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
