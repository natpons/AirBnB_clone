#!/usr/bin/python
"""Unittest for class BaseModel"""
import unittest
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """Defines tests for class BaseModel"""

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

if __name__ == '__main__':
    unittest.main()
