import unittest
from unittest.mock import patch, mock_open
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_invalid_text_type(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        invalid_input = 12345

        # Act & Assert
        with self.assertRaises(TypeError) as context:
            GetLanguage(invalid_input)
        self.assertIn("text must be a string", str(context.exception))

    @patch('your_module.load_dotenv')
    def test_get_language_empty_string(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        empty_input = ""

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            GetLanguage(empty_input)
        self.assertIn("text cannot be empty", str(context.exception))

    @patch('your_module.load_dotenv')
    def test_get_language_network_error(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        mock_request.urlopen.side_effect = error.URLError("Network Error")

        # Act & Assert
        with self.assertRaises(Exception) as context:
            GetLanguage("test text")
        self.assertIn("Network Error", str(context.exception))

if __name__ == '__main__':
    unittest.main()