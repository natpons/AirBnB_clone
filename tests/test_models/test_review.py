#!/usr/bin/python
"""Unittest for the class Review that inherits from BaseModel"""

import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review


class ReviewTest(unittest.TestCase):
    """Defines tests for the class Review"""

    def test_init_Review(self):
        """Test if instance of Review successfully made"""
        self.assertTrue(isinstance(Review(), Review))

    def test_attributes(self):
        """Test isinstance for all attributes"""
        self.assertEqual(type(Review().place_id), str)
        self.assertEqual(type(Review().user_id), str)
        self.assertEqual(type(Review().text), str)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/review.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(Review.__doc__)

if __name__ == '__main__':
    unittest.main()
