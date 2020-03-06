import os
from unittest import TestCase, mock

from core.utils.extractor import get_attribute
from tests.stubs import file_stub


class ExtractorTest(TestCase):

    def test_get_attribute_raise_type_error(self) -> None:
        """Assert that get_attribute method raises TypeError when the file is not .py.

        :return: None
        """
        with self.assertRaises(TypeError):
            get_attribute('/path/to/file.txt', 'file')

    def test_get_attribute_raises_os_error(self) -> None:
        """Assert that get_attribute method raises OSError when the file is non existing.

        :return:
        """
        with self.assertRaises(OSError):
            get_attribute('/path/to/file_stub.py', 'attribute')

    def test_get_attributes_success(self) -> None:
        """Assert that the value that is extracted from the path to file,
         is equal to the attribute of the actual file.

        :return: None
        """
        file = f'{os.path.dirname(os.path.abspath(__file__))}/../stubs/file_stub.py'
        self.assertEqual(file_stub.attribute_name, get_attribute(file, 'attribute_name'))
