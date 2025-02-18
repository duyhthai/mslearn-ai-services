import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    
    @patch('urllib.request.urlopen')
    def test_get_language_with_valid_response(self, mock_urlopen):
        mock_response = mock.Mock()
        mock_response.read.return_value = '{"language": "English"}'
        mock_urlopen.return_value = mock_response
        
        result = GetLanguage("test text")
        
        mock_urlopen.assert_called_once_with('http://example.com/get_language?text=test%20text')
        self.assertEqual(result, "English")

    @patch('urllib.request.urlopen', side_effect=error.URLError)
    def test_get_language_with_url_error(self, mock_urlopen):
        with self.assertRaises(error.URLError):
            GetLanguage("test text")

    @patch('urllib.request.urlopen', side_effect=error.HTTPError)
    def test_get_language_with_http_error(self, mock_urlopen):
        with self.assertRaises(error.HTTPError):
            GetLanguage("test text")

if __name__ == '__main__':
    unittest.main()