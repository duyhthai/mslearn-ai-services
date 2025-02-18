import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    @patch.dict('os.environ', {'LANGUAGE_MODEL_API_KEY': 'test_key'})
    def test_get_language_with_valid_text(self):
        text = "Hello, how are you?"
        expected_output = "English"
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = '{"language": "English"}'.encode()
            result = GetLanguage(text)
            self.assertEqual(result, expected_output)

    @patch.dict('os.environ', {'LANGUAGE_MODEL_API_KEY': 'test_key'})
    def test_get_language_with_empty_text(self):
        text = ""
        expected_output = None
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = '{}'.encode()
            result = GetLanguage(text)
            self.assertIsNone(result)

    @patch.dict('os.environ', {'LANGUAGE_MODEL_API_KEY': 'test_key'})
    def test_get_language_with_error_response(self):
        text = "Hello, how are you?"
        expected_output = None
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.status = 500
            mock_response.read.return_value = b'Internal Server Error'
            result = GetLanguage(text)
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()