import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):
    
    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_get_language_with_valid_text(self):
        text = "Hello, world!"
        expected_result = "en"
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = '{"language": "en"}'
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_get_language_with_empty_text(self):
        text = ""
        expected_result = None
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = '{"language": null}'
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_get_language_with_error(self):
        text = "Hello, world!"
        expected_result = None
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_connection.side_effect = Exception("Request failed")
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()