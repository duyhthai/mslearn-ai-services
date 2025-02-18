import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_empty_text(self, mock_load_dotenv):
        result = GetLanguage("")
        self.assertEqual(result, None)

    @patch('your_module.load_dotenv')
    def test_get_language_max_length_text(self, mock_load_dotenv):
        max_length_text = "a" * 10000
        result = GetLanguage(max_length_text)
        self.assertEqual(result, None)

    @patch('your_module.load_dotenv')
    def test_get_language_with_language_tag(self, mock_load_dotenv):
        text_with_language = "<lang>English</lang>"
        result = GetLanguage(text_with_language)
        self.assertEqual(result, "English")

if __name__ == '__main__':
    unittest.main()