import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    @patch('dotenv.load_dotenv')
    def test_main_with_valid_inputs(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'http://example.com'
        os.environ['AI_KEY'] = 'valid_api_key'

        # Act
        main()

        # Assert
        mock_load_dotenv.assert_called_once()
        self.assertEqual(os.getenv('AI_ENDPOINT'), 'http://example.com')
        self.assertEqual(os.getenv('AI_KEY'), 'valid_api_key')

    @patch('os.getenv')
    def test_main_without_ai_endpoint(self, mock_getenv):
        # Arrange
        mock_getenv.side_effect = [None, 'valid_api_key']

        # Act & Assert
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_without_ai_key(self, mock_getenv):
        # Arrange
        mock_getenv.side_effect = ['http://example.com', None]

        # Act & Assert
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()