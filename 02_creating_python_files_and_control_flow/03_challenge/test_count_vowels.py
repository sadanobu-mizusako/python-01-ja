import io
import unittest
from unittest.mock import patch


class TestFunction(unittest.TestCase):
    @patch("builtins.input", lambda _:"Hello world!")
    def test_convert(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            import count_vowels

            count_vowels

            printed_output = mock_stdout.getvalue().strip()

            expected_output = "Number of vowels: 3"
            self.assertEqual(printed_output, expected_output)


if __name__ == "__main__":
    unittest.main()
