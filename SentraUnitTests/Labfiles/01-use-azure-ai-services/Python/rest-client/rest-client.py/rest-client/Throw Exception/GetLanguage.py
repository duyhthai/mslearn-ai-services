import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_exception(self, mock_load_dotenv):
        mock_load_dotenv.side_effect = EnvironmentError("Failed to load environment variables")
        with self.assertRaises(EnvironmentError) as context:
            GetLanguage("test text")
        self.assertIn("Failed to load environment variables", str(context.exception))

    @patch('urllib.request.urlopen')
    def test_get_language_http_error(self, mock_open):
        mock_open.side_effect = error.HTTPError('http://example.com', 500, 'Internal Server Error', {}, None)
        with self.assertRaises(error.HTTPError) as context:
            GetLanguage("test text")
        self.assertEqual(context.exception.code, 500)

    @patch('urllib.request.urlopen')
    def test_get_language_parse_error(self, mock_open):
        mock_open.return_value.read.return_value = b'Invalid JSON response'
        with self.assertRaises(ValueError) as context:
            GetLanguage("test text")
        self.assertIn('Expecting property name enclosed in double quotes', str(context.exception))

if __name__ == '__main__':
    unittest.main()