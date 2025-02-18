import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    @patch('os.getenv')
    def test_get_language_with_invalid_text_type(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(TypeError):
            GetLanguage(123)

    @patch('os.getenv')
    def test_get_language_with_empty_text(self, mock_getenv):
        mock_getenv.return_value = None
        result = GetLanguage('')
        self.assertEqual(result, 'English')

    @patch('os.getenv')
    def test_get_language_with_unsupported_text(self, mock_getenv):
        mock_getenv.return_value = None
        result = GetLanguage('This text is in an unsupported language.')
        self.assertEqual(result, 'English')

if __name__ == '__main__':
    unittest.main()