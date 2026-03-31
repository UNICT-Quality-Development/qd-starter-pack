import unittest
from unittest.mock import patch
from io import StringIO
from src.convert_to_binary import convert_to_binary

class TestConvertToBinary(unittest.TestCase):
 @patch("builtins.input", return_value="5")
 @patch("sys.stdout", new_callable=StringIO)
 def test_convert_to_binary(self, mock_stdout, mock_input):
  convert_to_binary()
  output = mock_stdout.getvalue().strip()
  self.assertEqual(output, "The binary number is: 101")
 if __name__ == "__main__":
 unittest.main()
