import unittest
from unittest.mock import patch
from io import StringIO

class TestGetLanguage(unittest.TestCase):

    @patch('os.getenv')
    def test_get_language_empty_text(self, mock_getenv):
        mock_getenv.return_value = 'your_api_key'
        from your_module import GetLanguage
        result = GetLanguage("")
        self.assertEqual(result, "No language detected")

    @patch('os.getenv')
    def test_get_language_single_word(self, mock_getenv):
        mock_getenv.return_value = 'your_api_key'
        from your_module import GetLanguage
        result = GetLanguage("Hello")
        self.assertIn("en", result)

    @patch('os.getenv')
    def test_get_language_multiple_languages(self, mock_getenv):
        mock_getenv.return_value = 'your_api_key'
        from your_module import GetLanguage
        result = GetLanguage("Hello, how are you?")
        self.assertIn("en", result)

if __name__ == '__main__':
    unittest.main()