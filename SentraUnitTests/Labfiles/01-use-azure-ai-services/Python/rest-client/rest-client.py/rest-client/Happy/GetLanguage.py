import unittest
from unittest.mock import patch, mock_open
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):
    @patch('your_module.load_dotenv')
    def test_get_language_with_valid_input(self, mock_load_dotenv):
        # Arrange
        text = "Hello, world!"
        expected_result = "en"
        
        # Mocking environment variables
        mock_env = {'LANGUAGE': 'en'}
        mock_load_dotenv.return_value = None
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertEqual(result, expected_result)

    @patch('your_module.load_dotenv')
    def test_get_language_with_empty_input(self, mock_load_dotenv):
        # Arrange
        text = ""
        expected_result = None
        
        # Mocking environment variables
        mock_env = {'LANGUAGE': ''}
        mock_load_dotenv.return_value = None
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertIsNone(result)

    @patch('your_module.load_dotenv')
    def test_get_language_with_invalid_input(self, mock_load_dotenv):
        # Arrange
        text = "こんにちは、世界！"
        expected_result = None
        
        # Mocking environment variables
        mock_env = {'LANGUAGE': ''}
        mock_load_dotenv.return_value = None
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()