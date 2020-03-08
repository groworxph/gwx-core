import os
from gwx_core.utils import stringify
from tests.utils_test_case import UtilsTestCase


class StringifyTest(UtilsTestCase):

    def setUp(self) -> None:
        self.stub = f'{os.path.abspath(os.getcwd())}/../stubs/file_stub.py'
        self.stub_name = 'file_stub'

    def test_file_name_conversion_successfully(self) -> None:
        """Assert that the file name from an absolute path has been extracted,
        without the file extension ie: `.py`.

        :return: None
        """

        file_name = stringify.file_name_conversion(self.stub)
        self.assertEqual('file_stub', file_name)

    def test_file_name_conversion_with_extension_params_successfully(self) -> None:
        """Assert that the file name from an absolute path has been extracted,
        without the file extension ie: `.py`, and it's extended name removed ie: `_stub`

        :return:
        """
        file_name = stringify.file_name_conversion(self.stub, '_stub')
        self.assertEqual('file', file_name)

    def test_file_name_conversion_raise_exception(self) -> None:
        """Assert that the FileNotFoundError exception is raised,
        when a non existing file is submitted as parameter.

        :return: None
        """

        non_existing_file = '/path/to/non_existing_file.py'
        with self.assertRaises(FileNotFoundError) as context:
            stringify.file_name_conversion(non_existing_file)

        self.assertEqual(f'Error file: {non_existing_file} does not exists.', str(context.exception))

    def test_pascal_case_successful(self) -> None:
        """Assert that the pascal case handles conversion of words separated by underscores `_` or spaces ` `.

        :return: None
        """
        self.assertEqual('FileFile', stringify.pascal_case(f'{self.stub_name[:-4]} {self.stub_name[:-4]}'))
        self.assertEqual('File', stringify.pascal_case(self.stub_name[:-4]))
        self.assertEqual('FileStub', stringify.pascal_case(self.stub_name))
