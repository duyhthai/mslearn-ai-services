import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    
    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_get_language_with_valid_text(self):
        text = "Hello, how are you?"
        expected_result = "English"
        with patch('http.request.urlopen') as mock_request:
            mock_request.return_value.read.return_value.decode.return_value = '{"language": "English"}'
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_get_language_with_empty_text(self):
        text = ""
        expected_result = None
        with patch('http.request.urlopen') as mock_request:
            mock_request.side_effect = error.URLError("URL Error")
            result = GetLanguage(text)
            self.assertIsNone(result)

    @patch.dict('os.environ', {'API_KEY': 'test_key'})
    def test_get_language_with_invalid_api_response(self):
        text = "Hello, how are you?"
        expected_result = None
        with patch('http.request.urlopen') as mock_request:
            mock_request.return_value.read.return_value.decode.return_value = '{"error": "Invalid input"}'
            result = GetLanguage(text)
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()