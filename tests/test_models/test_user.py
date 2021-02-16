#!/usr/bin/python
"""Unittest for the class  User that inherits from BaseModel"""

import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class UserTest(unittest.TestCase):
    """Defines tests for the class User"""

    def test_init_User(self):
        """Test if instance of User successfully made"""
        self.assertTrue(isinstance(User(), User))

    def test_instance(self):
        """Test isinstance for all attributes"""
        self.assertIsInstance(User().email, str)
        self.assertIsInstance(User().password, str)
        self.assertIsInstance(User().first_name, str)
        self.assertIsInstance(User().last_name, str)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/user.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(User.__doc__)

if __name__ == '__main__':
    unittest.main()
