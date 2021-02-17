#!/usr/bin/python
"""Unittest for the class State that inherits from BaseModel"""

import unittest
import pep8
from models.base_model import BaseModel
from models.state import State


class StateTest(unittest.TestCase):
    """Defines tests for the class User"""

    def test_init_State(self):
        """Test if instance of State successfully made"""
        self.assertTrue(isinstance(State(), State))

    def test_instance(self):
        """Test isinstance for all attributes"""
        self.assertIsInstance(State().name, str)

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/state.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertIsNotNone(State.__doc__)

if __name__ == '__main__':
    unittest.main()
