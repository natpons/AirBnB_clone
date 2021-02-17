#!/usr/bin/python
"""Unittest for the class Place that inherits from BaseModel"""

import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place


class PlaceTest(unittest.TestCase):
    """Defines tests for the class Place"""

    def test_init_Place(self):
        """Test if instance of Place successfully made"""
        self.assertTrue(isinstance(Place(), Place))

    def test_attributes(self):
        """Test isinstance for all attributes"""
        self.assertEqual(type(Place().city_id), str)
        self.assertEqual(type(Place().user_id), str)
        self.assertEqual(type(Place().name), str)
        self.assertEqual(type(Place().description), str)
        self.assertEqual(type(Place().number_rooms), int)
        self.assertEqual(type(Place().number_bathrooms), int)
        self.assertEqual(type(Place().max_guest), int)
        self.assertEqual(type(Place().price_by_night), int)
        self.assertEqual(type(Place().latitude), float)
        self.assertEqual(type(Place().longitude), float)
        self.assertEqual(type(Place().amenity_ids), list)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/place.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(Place.__doc__)

if __name__ == '__main__':
    unittest.main()
