# Unit tests for the main function from the provided source code
import unittest
from unittest.mock import patch, mock_open
from io import StringIO

class TestMain(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_load_dotenv(self, mock_file):
        # Arrange
        mock_file.return_value.__enter__.return_value.read.return_value = "AI_ENDPOINT=http://example.com\nAI_KEY=12345"
        
        # Act
        main()
        
        # Assert
        self.assertEqual(os.getenv('AI_ENDPOINT'), 'http://example.com')
        self.assertEqual(os.getenv('AI_KEY'), '12345')

    def test_main_without_environment_variables(self):
        # Arrange
        with patch.dict('os.environ', {}, clear=True):
            pass
        
        # Act & Assert
        with self.assertRaises(KeyError):
            main()

if __name__ == '__main__':
    unittest.main()