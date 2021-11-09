#!/usr/bin/python3
""" Unit tests for AirBnB console """

import unittest
import console
import pep8


class Test_Amenity(unittest.TestCase):
    """Base class tests"""

    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8pattern = pep8.StyleGuide(quiet=True)
        result = pep8pattern.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code patterns errors (and warnings).")

    def test_docstring(self):
        """ Test documentation """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(console.HBNBCommand.__doc__)

if __name__ == '__main__':
    unittest.main()
