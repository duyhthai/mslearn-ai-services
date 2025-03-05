import unittest
from unittest.mock import patch, MagicMock
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('dotenv.load_dotenv')
    def test_main_with_valid_env(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'http://example.com'
        os.environ['AI_KEY'] = 'valid_key'

        # Act
        main()

        # Assert
        mock_load_dotenv.assert_called_once()
        self.assertIn('AI_ENDPOINT', os.environ)
        self.assertIn('AI_KEY', os.environ)

    @patch('dotenv.load_dotenv')
    def test_main_without_env(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ.pop('AI_ENDPOINT', None)
        os.environ.pop('AI_KEY', None)

        # Act & Assert
        with self.assertRaises(KeyError):
            main()

    @patch('dotenv.load_dotenv')
    def test_main_with_invalid_env(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'invalid_url'
        os.environ['AI_KEY'] = 'valid_key'

        # Act & Assert
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()