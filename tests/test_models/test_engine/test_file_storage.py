#!/usr/bin/python
"""Unittest for the class FileStorage"""

import unittest
import pep8
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class FileStorageTest(unittest.TestCase):
    """Defines tests for class BaseModel"""

    def test_init_FileStorage(self):
        """Test if instance of FileStorage successfully made"""
        self.assertTrue(isinstance(FileStorage(), FileStorage))

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/engine/file_storage.py'])
        st = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, st)

    def test_method(self):
        """Test FileStorage methods"""
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        """Test the all method"""

    def test_new(self):
        """Tests the new method"""

    def test_save(self):
        """Tests for the save method"""

    def test_reload(self):
        """Tests for the reload method"""

if __name__ == '__main__':
    unittest.main()
