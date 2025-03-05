import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    
    @patch('dotenv.load_dotenv')
    def test_main_with_valid_env_vars(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'https://example.com'
        os.environ['AI_KEY'] = 'valid_key'

        # Act
        main()

        # Assert
        # Assuming main does something with ai_endpoint and ai_key
        self.assertIn('AI_ENDPOINT', os.environ)
        self.assertIn('AI_KEY', os.environ)

    @patch('dotenv.load_dotenv')
    def test_main_without_ai_endpoint(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ.pop('AI_ENDPOINT', None)
        os.environ['AI_KEY'] = 'valid_key'

        # Act & Assert
        with self.assertRaises(KeyError):
            main()

    @patch('dotenv.load_dotenv')
    def test_main_without_ai_key(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'https://example.com'
        os.environ.pop('AI_KEY', None)

        # Act & Assert
        with self.assertRaises(KeyError):
            main()

if __name__ == '__main__':
    unittest.main()