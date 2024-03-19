import unittest
from unittest import mock
from unittest.mock import patch
import io
from temp_convert import convert


class TestFunction(unittest.TestCase):
    @patch("builtins.input", side_effect=[0, "c"])
    def test_temp_convert_c_to_f(self, mock_inputs):
        res = convert()
        self.assertEqual(res, 32.0)

    @patch("builtins.input", side_effect=[32, "f"])
    def test_temp_convert_f_to_c(self, mock_inputs):
        res = convert()
        self.assertEqual(res, 0.0)


if __name__ == "__main__":
    unittest.main()
