import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_language_success(self, mock_open):
        mock_response = type('Response', (), {'read': lambda self: '{"language": "English"}'})
        mock_open.return_value = mock_response
        
        text = "Hello World"
        result = GetLanguage(text)
        
        mock_open.assert_called_once_with('https://api.example.com/language?text=Hello%20World')
        self.assertEqual(result, "English")

    @patch('urllib.request.urlopen')
    def test_get_language_error(self, mock_open):
        mock_open.side_effect = error.URLError("Mocked Error")
        
        text = "Hello World"
        result = GetLanguage(text)
        
        mock_open.assert_called_once_with('https://api.example.com/language?text=Hello%20World')
        self.assertIsNone(result)

    @patch('urllib.parse.quote')
    def test_get_language_empty_text(self, mock_quote):
        mock_quote.return_value = ""
        
        text = ""
        result = GetLanguage(text)
        
        mock_quote.assert_not_called()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()