# Import necessary libraries
import unittest
from unittest.mock import patch
from your_module_name import main  # Replace 'your_module_name' with actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_missing_ai_endpoint(self, mock_getenv):
        # Arrange
        mock_getenv.side_effect = lambda key: None if key == 'AI_ENDPOINT' else 'some_value'
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch('os.getenv')
    def test_invalid_ai_key_type(self, mock_getenv):
        # Arrange
        mock_getenv.side_effect = lambda key: 'not_a_string' if key == 'AI_KEY' else 'some_value'
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch('http.request.urlopen')
    def test_http_request_error(self, mock_urlopen):
        # Arrange
        mock_urlopen.side_effect = error.URLError("Test Error")
        
        # Act & Assert
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()