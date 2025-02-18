import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('http.request.urlopen')
    def test_get_language_with_invalid_text_type(self, mock_request):
        # Arrange
        text = 123  # Invalid input type (integer)
        expected_exception = TypeError
        
        # Act & Assert
        with self.assertRaises(expected_exception) as context:
            GetLanguage(text)
        
        # Additional assertion to check the exception message if needed
        self.assertIn("invalid literal for int() with base 10", str(context.exception))

    @patch('http.request.urlopen')
    def test_get_language_with_empty_text(self, mock_request):
        # Arrange
        text = ""  # Empty string
        expected_exception = ValueError
        
        # Act & Assert
        with self.assertRaises(expected_exception) as context:
            GetLanguage(text)
        
        # Additional assertion to check the exception message if needed
        self.assertIn("Text cannot be empty", str(context.exception))

    @patch('http.request.urlopen')
    def test_get_language_with_http_error(self, mock_request):
        # Arrange
        mock_request.side_effect = error.HTTPError(url=None, code=404, msg="Not Found", hdrs={}, reason="Not Found")
        text = "test"
        
        # Act & Assert
        with self.assertRaises(error.HTTPError) as context:
            GetLanguage(text)
        
        # Additional assertion to check the exception message if needed
        self.assertEqual(404, context.exception.code)

if __name__ == '__main__':
    unittest.main()