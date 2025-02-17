import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_invalid_text_type(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        invalid_text = 123

        # Act & Assert
        with self.assertRaises(TypeError):
            GetLanguage(invalid_text)

    @patch('your_module.load_dotenv')
    def test_get_language_empty_string(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        empty_text = ""

        # Act & Assert
        with self.assertRaises(ValueError):
            GetLanguage(empty_text)

    @patch('your_module.load_dotenv')
    def test_get_language_non_existent_language(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        non_existent_text = "nonexistentlanguage"

        # Act & Assert
        with self.assertRaises(KeyError):
            GetLanguage(non_existent_text)

if __name__ == '__main__':
    unittest.main()