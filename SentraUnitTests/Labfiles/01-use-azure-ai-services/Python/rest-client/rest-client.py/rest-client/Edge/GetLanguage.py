import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    
    @patch.dict('os.environ', {'LANGUAGE_API_KEY': 'test_key'})
    def test_get_language_with_valid_text(self):
        text = "Hello, world!"
        response_data = '{"language": "English"}'
        
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = response_data.encode()
            
            result = GetLanguage(text)
            self.assertEqual(result, "English")
            mock_connection.assert_called_once_with("api.example.com", 443)
            mock_connection.return_value.request.assert_called_once_with(
                "GET",
                "/v1/language?text=Hello%2C+world!",
                headers={'Authorization': 'Bearer test_key'}
            )
            mock_response.read.assert_called_once()

    @patch.dict('os.environ', {'LANGUAGE_API_KEY': 'test_key'})
    def test_get_language_with_empty_text(self):
        text = ""
        response_data = '{"language": "Unknown"}'
        
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = response_data.encode()
            
            result = GetLanguage(text)
            self.assertEqual(result, "Unknown")
            mock_connection.assert_not_called()

    @patch.dict('os.environ', {'LANGUAGE_API_KEY': 'test_key'})
    def test_get_language_with_api_error(self):
        text = "Hello, world!"
        
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_connection.side_effect = Exception("API Error")
            
            result = GetLanguage(text)
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()