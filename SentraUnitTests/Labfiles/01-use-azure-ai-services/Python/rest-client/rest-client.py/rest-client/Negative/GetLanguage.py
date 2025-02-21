import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_language_with_invalid_url(self, mock_urlopen):
        mock_urlopen.side_effect = error.URLError("Invalid URL")
        with self.assertRaises(error.URLError):
            GetLanguage("Hello world")

    @patch('urllib.parse.urlencode')
    @patch('urllib.request.urlopen')
    def test_get_language_with_http_error(self, mock_urlopen, mock_encode):
        response = http.client.HTTPResponse()
        response.status = 400
        mock_urlopen.return_value = response
        with self.assertRaises(http.client.HTTPError):
            GetLanguage("Hello world")

    @patch('urllib.parse.urlencode')
    @patch('urllib.request.urlopen')
    def test_get_language_with_empty_response(self, mock_urlopen, mock_encode):
        response = http.client.HTTPResponse()
        response.status = 200
        response.read.return_value = b''
        mock_urlopen.return_value = response
        with self.assertRaises(ValueError):
            GetLanguage("Hello world")

if __name__ == '__main__':
    unittest.main()