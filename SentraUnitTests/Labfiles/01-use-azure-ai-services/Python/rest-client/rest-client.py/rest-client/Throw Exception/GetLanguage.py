import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_with_error(self, mock_load_dotenv):
        mock_load_dotenv.side_effect = EnvironmentError("Failed to load .env file")
        with self.assertRaises(EnvironmentError) as context:
            GetLanguage("test text")
        self.assertIn("Failed to load .env file", str(context.exception))

    @patch('urllib.request.urlopen')
    def test_get_language_with_http_error(self, mock_open_url):
        mock_open_url.side_effect = error.URLError("HTTP Error 404: Not Found")
        with self.assertRaises(error.URLError) as context:
            GetLanguage("test text")
        self.assertIn("HTTP Error 404: Not Found", str(context.exception))

    @patch('urllib.parse.urlencode')
    def test_get_language_with_parse_error(self, mock_encode):
        mock_encode.side_effect = TypeError("Invalid input type")
        with self.assertRaises(TypeError) as context:
            GetLanguage("test text")
        self.assertIn("Invalid input type", str(context.exception))

if __name__ == '__main__':
    unittest.main()