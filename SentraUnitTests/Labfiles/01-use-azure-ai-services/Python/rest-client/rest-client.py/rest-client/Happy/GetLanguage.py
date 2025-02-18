import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')
    def test_get_language_valid_input(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        text = "Hello, how are you?"
        result = GetLanguage(text)
        self.assertEqual(result, "English")  # Assuming English detection

    @patch('your_module.load_dotenv')
    def test_get_language_empty_string(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        text = ""
        result = GetLanguage(text)
        self.assertEqual(result, "Unknown")

    @patch('your_module.load_dotenv')
    def test_get_language_error_handling(self, mock_load_dotenv):
        mock_load_dotenv.side_effect = Exception("Error loading environment variables")
        text = "Hello, how are you?"
        with self.assertRaises(Exception) as context:
            GetLanguage(text)
        self.assertTrue("Error loading environment variables" in str(context.exception))

if __name__ == '__main__':
    unittest.main()