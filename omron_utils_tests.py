from unittest import TestCase
import omron_utils

class TestUtils(TestCase):
    def test_extract_int_value_from_hex_string(self):
        self.common_test("47DC", 1, 9 , 144)
        self.common_test("4581", 1, 9, 139)
        self.common_test("444E", 1, 9, 137)

        self.common_test("2697", 1, 9, 77)
        self.common_test("24E6", 1, 9, 74)
        self.common_test("2899", 1, 9, 81)

    def common_test(self, test_input, index_from, index_to, expectedResult):
        result = omron_utils.extract_int_value_from_hex_string(test_input, index_from, index_to)
        self.assertAlmostEqual(expectedResult, result, delta=1)
        result = omron_utils.get_float_value_from_hex(test_input)
        self.assertAlmostEqual(expectedResult, result, delta=1)
