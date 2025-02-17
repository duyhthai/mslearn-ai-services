import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):
    @patch('your_module.load_dotenv')
    def test_get_language_exception(self, mock_load_dotenv):
        mock_load_dotenv.side_effect = Exception("Failed to load environment variables")
        with self.assertRaises(Exception) as context:
            GetLanguage("test text")
        self.assertIn("Failed to load environment variables", str(context.exception))

    @patch('os.getenv')
    def test_get_language_no_api_key(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(ValueError) as context:
            GetLanguage("test text")
        self.assertIn("API key not found in environment variables", str(context.exception))

    @patch('http.client.HTTPSConnection')
    def test_get_language_http_error(self, mock_connection):
        mock_connection().request.side_effect = error.URLError("HTTP Error")
        with self.assertRaises(error.URLError) as context:
            GetLanguage("test text")
        self.assertIn("HTTP Error", str(context.exception))

if __name__ == '__main__':
    unittest.main()