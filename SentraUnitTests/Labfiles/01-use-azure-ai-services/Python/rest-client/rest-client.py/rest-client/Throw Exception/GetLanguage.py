import unittest
from unittest.mock import patch, MagicMock
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_language_with_valid_input(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"language": "English"}'
        mock_urlopen.return_value = mock_response
        
        result = GetLanguage("Hello World")
        
        self.assertEqual(result, "English")

    @patch('urllib.request.urlopen', side_effect=error.URLError)
    def test_get_language_with_network_error(self, mock_urlopen):
        with self.assertRaises(error.URLError):
            GetLanguage("Hello World")

    @patch('urllib.request.urlopen', side_effect=http.HTTPError(url="http://example.com", code=404, msg="Not Found", headers={}))
    def test_get_language_with_http_404_error(self, mock_urlopen):
        with self.assertRaises(http.HTTPError):
            GetLanguage("Hello World")

if __name__ == '__main__':
    unittest.main()