#!/usr/bin/python
"""Unittest for the class City that inherits from BaseModel"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City


class CityTest(unittest.TestCase):
    """Defines tests for the class City"""

    def test_init_City(self):
        """Test if instance of City successfully made"""
        self.assertTrue(isinstance(City(), City))

    def test_attributes(self):
        """Test isinstance for all attributes"""
        self.assertEqual(type(City().state_id), str)
        self.assertEqual(type(City().name), str)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/city.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(City.__doc__)

if __name__ == '__main__':
    unittest.main()
