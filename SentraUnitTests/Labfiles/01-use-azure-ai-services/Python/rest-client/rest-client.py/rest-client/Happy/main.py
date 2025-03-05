import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name where main is defined

class TestMain(unittest.TestCase):
    @patch('dotenv.load_dotenv')
    def test_main_with_valid_inputs(self, mock_load_dotenv):
        # Arrange
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'https://example.com/api'
        os.environ['AI_KEY'] = 'valid_api_key'

        # Act
        main()

        # Assert
        mock_load_dotenv.assert_called_once()
        self.assertIn('AI_ENDPOINT', os.environ)
        self.assertIn('AI_KEY', os.environ)

if __name__ == '__main__':
    unittest.main()