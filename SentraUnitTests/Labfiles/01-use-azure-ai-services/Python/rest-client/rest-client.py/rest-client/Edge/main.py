import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    @patch('dotenv.load_dotenv')
    def test_main_with_valid_environment_variables(self, mock_load_dotenv):
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
    def test_main_without_environment_variables(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ.pop('AI_ENDPOINT', None)
        os.environ.pop('AI_KEY', None)

        # Act
        main()

        # Assert
        mock_load_dotenv.assert_called_once()
        self.assertNotIn('AI_ENDPOINT', os.environ)
        self.assertNotIn('AI_KEY', os.environ)

    @patch('dotenv.load_dotenv')
    def test_main_with_empty_environment_variables(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = ''
        os.environ['AI_KEY'] = ''

        # Act
        main()

        # Assert
        mock_load_dotenv.assert_called_once()
        self.assertEqual(os.environ['AI_ENDPOINT'], '')
        self.assertEqual(os.environ['AI_KEY'], '')

if __name__ == '__main__':
    unittest.main()