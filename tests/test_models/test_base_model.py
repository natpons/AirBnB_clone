#!/usr/bin/python
"""Unittest for class BaseModel"""

import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """Defines tests for class BaseModel"""

    def test_init_BaseModel(self):
        """Test if instance of BaseModel successfully made"""
        self.assertTrue(isinstance(BaseModel(), BaseModel))

    def test_instance(self):
        """Test isinstance for all attributes"""
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().created_at, datetime)
        self.assertIsInstance(BaseModel().updated_at, datetime)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/base_model.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method(self):
        """Test Basemodel methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_to_dict(self):
        """Test convert to dictionary"""
        my_dict = BaseModel().to_dict()
        self.assertEqual(BaseModel().__class__.__name__, 'BaseModel')
        self.assertIsInstance(my_dict['created_at'], str)
        self.assertIsInstance(my_dict['updated_at'], str)

    def test_id(self):
        """Tests for id: basic id init, is str, random"""
        self.assertIsNotNone(BaseModel().id)
        self.assertEqual(type(BaseModel().id), str)
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_created_at(self):
        """Tests for created_at"""
        self.assertIsNotNone(BaseModel().created_at)
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_updated_at(self):
        """Tests for created_at"""
        self.assertIsNotNone(BaseModel().updated_at)
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_str(self):
        """Tests for the str method"""
        self.assertIsNotNone(BaseModel().__str__)
        self.assertIsInstance(BaseModel().__str__(), str)

    def test_save(self):
        """Tests for the save method"""
        test1 = BaseModel().updated_at
        BaseModel().save()
        self.assertFalse(BaseModel().updated_at == test1)

    def test_to_dict(self):
        """Tests for to_dict method"""
        self.assertIsNotNone(BaseModel().to_dict())
        self.assertEqual(type(BaseModel().to_dict()), dict)
        self.assertEqual(type(BaseModel().to_dict()['created_at']), str)
        self.assertEqual(type(BaseModel().to_dict()['updated_at']), str)

if __name__ == '__main__':
    unittest.main()
