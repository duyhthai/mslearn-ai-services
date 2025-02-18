import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_language_with_invalid_url(self, mock_open):
        mock_open.side_effect = error.URLError("Invalid URL")
        with self.assertRaises(error.URLError):
            GetLanguage("test text")

    @patch('urllib.request.urlopen')
    def test_get_language_with_non_json_response(self, mock_open):
        mock_open.return_value.read.return_value = b"not json"
        with self.assertRaises(ValueError):
            GetLanguage("test text")

    @patch('urllib.request.urlopen')
    def test_get_language_with_missing_data_key(self, mock_open):
        mock_open.return_value.read.return_value = b'{"data": null}'
        with self.assertRaises(KeyError):
            GetLanguage("test text")

if __name__ == '__main__':
    unittest.main()