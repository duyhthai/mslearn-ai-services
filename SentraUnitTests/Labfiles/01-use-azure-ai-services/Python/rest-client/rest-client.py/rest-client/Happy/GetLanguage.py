import unittest
from unittest.mock import patch, mock_open
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_success(self, mock_load_dotenv):
        # Arrange
        text = "Hello, world!"
        mock_load_dotenv.return_value = None
        
        # Mocking environment variables
        with patch.dict(os.environ, {'LANGUAGE_API_KEY': 'test_key'}):
            # Mocking HTTP response
            mock_response = mock_open(read_data='{"language": "English"}')
            with patch('http.client.HTTPSConnection', return_value=mock_response) as mock_connection:
                mock_connection().request.return_value = None
                mock_connection().getresponse.return_value.read.return_value = '{"language": "English"}'
                
                # Act
                result = GetLanguage(text)
                
                # Assert
                self.assertEqual(result, 'English')

    @patch('your_module.load_dotenv')
    def test_get_language_failure(self, mock_load_dotenv):
        # Arrange
        text = "Hello, world!"
        mock_load_dotenv.return_value = None
        
        # Mocking environment variables
        with patch.dict(os.environ, {'LANGUAGE_API_KEY': 'test_key'}):
            # Mocking HTTP response
            mock_response = mock_open()
            with patch('http.client.HTTPSConnection', return_value=mock_response) as mock_connection:
                mock_connection().request.return_value = None
                mock_connection().getresponse.return_value.status = 500
                
                # Act & Assert
                with self.assertRaises(Exception):
                    GetLanguage(text)

    @patch('your_module.load_dotenv')
    def test_get_language_empty_text(self, mock_load_dotenv):
        # Arrange
        text = ""
        mock_load_dotenv.return_value = None
        
        # Mocking environment variables
        with patch.dict(os.environ, {'LANGUAGE_API_KEY': 'test_key'}):
            # Act & Assert
            with self.assertRaises(ValueError):
                GetLanguage(text)

if __name__ == '__main__':
    unittest.main()