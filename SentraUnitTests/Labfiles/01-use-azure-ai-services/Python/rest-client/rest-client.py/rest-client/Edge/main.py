import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_main_with_valid_env_variables(self, mock_file):
        # Arrange
        mock_file.return_value.__enter__.return_value.read.return_value = "AI_ENDPOINT=http://example.com\nAI_KEY=12345"
        os.environ['AI_ENDPOINT'] = ''
        os.environ['AI_KEY'] = ''

        # Act
        main()

        # Assert
        self.assertEqual(os.environ['AI_ENDPOINT'], 'http://example.com')
        self.assertEqual(os.environ['AI_KEY'], '12345')

    @patch('builtins.open', new_callable=mock_open)
    def test_main_with_missing_ai_endpoint(self, mock_file):
        # Arrange
        mock_file.return_value.__enter__.return_value.read.return_value = "AI_KEY=12345"
        os.environ['AI_ENDPOINT'] = ''
        os.environ['AI_KEY'] = ''

        # Act & Assert
        with self.assertRaises(SystemExit):
            main()

    @patch('builtins.open', new_callable=mock_open)
    def test_main_with_missing_ai_key(self, mock_file):
        # Arrange
        mock_file.return_value.__enter__.return_value.read.return_value = "AI_ENDPOINT=http://example.com"
        os.environ['AI_ENDPOINT'] = ''
        os.environ['AI_KEY'] = ''

        # Act & Assert
        with self.assertRaises(SystemExit):
            main()

if __name__ == '__main__':
    unittest.main()