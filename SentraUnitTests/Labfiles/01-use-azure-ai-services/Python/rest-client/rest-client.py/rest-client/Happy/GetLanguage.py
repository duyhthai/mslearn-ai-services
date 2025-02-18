import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):
    
    @patch('your_module.load_dotenv')
    def test_get_language_valid_input(self, mock_load_dotenv):
        # Arrange
        text = "Hello world"
        expected_output = "English"  # Assuming English is returned for "Hello world"

        # Mocking environment variables if needed
        mock_load_dotenv.return_value = None
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertEqual(result, expected_output)

    @patch('your_module.load_dotenv')
    def test_get_language_empty_string(self, mock_load_dotenv):
        # Arrange
        text = ""
        expected_output = ""  # Assuming empty string returns empty string
        
        # Mocking environment variables if needed
        mock_load_dotenv.return_value = None
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertEqual(result, expected_output)

    @patch('your_module.load_dotenv')
    def test_get_language_error_handling(self, mock_load_dotenv):
        # Arrange
        text = "Invalid input"
        expected_output = None  # Assuming None is returned on error
        
        # Mocking environment variables if needed
        mock_load_dotenv.return_value = None
        
        # Act
        result = GetLanguage(text)
        
        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()