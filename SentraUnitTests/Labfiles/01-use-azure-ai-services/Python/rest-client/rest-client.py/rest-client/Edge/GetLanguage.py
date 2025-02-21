import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_empty_text(self, mock_load_dotenv):
        result = GetLanguage("")
        self.assertEqual(result, None)

    @patch('your_module.load_dotenv')
    def test_get_language_single_word(self, mock_load_dotenv):
        result = GetLanguage("Python")
        self.assertEqual(result, "Python")

    @patch('your_module.load_dotenv')
    def test_get_language_complex_sentence(self, mock_load_dotenv):
        result = GetLanguage("Hello, how are you doing today?")
        self.assertEqual(result, "English")

if __name__ == '__main__':
    unittest.main()