#!/usr/bin/python
"""Unittest for the class Amenity that inherits from BaseModel"""

import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    """Defines tests for the class Amenity"""

    def test_init_Amenity(self):
        """Test if instance of Amenity successfully made"""
        self.assertTrue(isinstance(Amenity(), Amenity))

    def test_attributes(self):
        """Test isinstance for all attributes"""
        self.assertEqual(type(Amenity().name), str)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/amenity.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(Amenity.__doc__)

if __name__ == '__main__':
    unittest.main()
