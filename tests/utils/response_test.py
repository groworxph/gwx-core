from gwx_core.utils import response
from tests.UtilsTestCase import UtilsTestCase


class ResponseTest(UtilsTestCase):

    def test_create_raise_type_error(self) -> None:
        """Assert that the response.create method raises a type error,
        and the raised exception message matches the one specified for comparison.

        :return: None
        """

        self.assertRaiseWithMessageOnResponse(
            TypeError,
            response.create,
            "Invalid type: <class 'str'>, should be type <class 'dict'>",
            'This is a success',
            {'key': 'value'},
            'This should\'ve a dict type'
        )

    def test_create_successfully(self) -> None:
        """Assert that create returns a tuple value and that the value conforms with the
        dict, int, dict or None parametrized structure, and a  code value of 201.

        :return: None
        """
        result = response.create('This is created', {'key': 'value'})
        self.assertTupleEqual(
            result,
            (
                {'code': 201, 'data': {'key': 'value'}, 'message': 'This is created'},
                201,
                None
            )
        )

    def test_create_with_headers_successfully(self) -> None:
        """Assert that the create returns a tuple value and that the value conforms with the
        dict, int, dict or None parametrized structure,
        a code value 201 and returns the header value defined.

        :return: None
        """
        result = response.create(
            'This is created successfully',
            {'key': 'value'},
            {'Gwx-Header-Sample': 'This is a sample create header value'}
        )

        self.assertTupleEqual(
            result,
            (
                {'code': 201, 'data': {'key': 'value'}, 'message': 'This is created successfully'},
                201,
                {'Gwx-Header-Sample': 'This is a sample create header value'}
            )
        )

    def test_not_found_successfully(self) -> None:
        """Assert the not found returns a tuple value and that the value conforms with the
        None, int, dict or None parametrized structure, and a  code value of 404.

        :return: None
        """
        result = response.not_found('This is a update success with no content', {'key': 'value'})
        self.assertTupleEqual(
            result,
            (
                {'code': 404, 'data': {'key': 'value'}, 'message': 'This is a update success with no content'},
                404,
                None
            )
        )

    def test_success_successfully(self) -> None:
        """Assert the success returns a tuple value and that the value conforms with the
        dict, int, dict or None parametrized structure, and a  code value of 200.

        :return: None
        """
        result = response.success('This is a success', {'key': 'value'})
        self.assertTupleEqual(
            result,
            (
                {'code': 200, 'data': {'key': 'value'}, 'message': 'This is a success'},
                200,
                None
            )
        )

    def test_update_no_content_successfully(self) -> None:
        """Assert the update returns a tuple value and that the value conforms with the
        None, int, dict or None parametrized structure, and a  code value of 203.

        :return: None
        """
        result = response.update_success_no_content('This is a update success with no content')
        self.assertTupleEqual(
            result,
            (
                {'code': 203, 'data': None, 'message': 'This is a update success with no content'},
                203,
                None
            )
        )

    def test_success_with_headers_successfully(self) -> None:
        """Assert the success returns a tuple value and that the value conforms with the
        dict, int, dict or None parametrized structure,
        a code value 200 and returns the header value defined.

        :return: None
        """
        result = response.success(
            'This is a success',
            {'key': 'value'},
            {'Gwx-Header-Sample': 'This is a sample header value'}
        )

        self.assertTupleEqual(
            result,
            (
                {'code': 200, 'data': {'key': 'value'}, 'message': 'This is a success'},
                200,
                {'Gwx-Header-Sample': 'This is a sample header value'}
            )
        )

    def test_success_raise_type_error(self) -> None:
        """Assert that the response.success method raises a type error,
        and the raised exception message matches the one specified for comparison.

        :return: None
        """

        self.assertRaiseWithMessageOnResponse(
            TypeError,
            response.success,
            "Invalid type: <class 'str'>, should be type <class 'dict'>",
            'This is a success',
            {'key': 'value'},
            'This should\'ve a dict type'
        )
