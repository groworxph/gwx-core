from gwx_core.utils.rates_calculator import calculate_supplier_service_rate
from tests.utils_test_case import UtilsTestCase


class RatesCalculatorTest(UtilsTestCase):

    def test_calculate_supplier_service_rate_successfully(self) -> None:
        """Assert that the return value is float and is what is expected based on the computation.

        :return: None
        """
        result = calculate_supplier_service_rate(100, 500)

        self.assertIs(type(result), float)
        self.assertEqual(1000.0, result)

    def test_calculate_supplier_service_rate_is_int_successfully(self) -> None:
        """Assert that the return value is float and is what is expected based on the computation.

        :return: None
        """
        result = calculate_supplier_service_rate(100, 500, True)

        self.assertIs(type(result), int)
        self.assertEqual(1000, result)
