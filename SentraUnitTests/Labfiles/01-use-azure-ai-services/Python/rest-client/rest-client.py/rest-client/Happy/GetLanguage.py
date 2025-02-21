import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_language_valid_input(self, mock_open):
        # Arrange
        text = "Hello, how are you?"
        mock_response = mock_open.return_value.__enter__.return_value
        mock_response.read.return_value = b'{"language": "English"}'
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertEqual(result, "English")

    @patch('urllib.request.urlopen')
    def test_get_language_invalid_input(self, mock_open):
        # Arrange
        text = "こんにちは、どのようにですか？"
        mock_response = mock_open.return_value.__enter__.return_value
        mock_response.read.side_effect = error.URLError("URL Error")
        
        # Act & Assert
        with self.assertRaises(error.URLError):
            GetLanguage(text)

    @patch('urllib.request.urlopen')
    def test_get_language_empty_response(self, mock_open):
        # Arrange
        text = "Hello, how are you?"
        mock_response = mock_open.return_value.__enter__.return_value
        mock_response.read.return_value = b''
        
        # Act & Assert
        with self.assertRaises(ValueError):
            GetLanguage(text)

if __name__ == '__main__':
    unittest.main()