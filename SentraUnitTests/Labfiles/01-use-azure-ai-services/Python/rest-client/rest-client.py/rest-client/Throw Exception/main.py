import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_main_loads_environment_variables(self, mock_file):
        # Arrange
        mock_file.return_value.read.return_value = "AI_ENDPOINT=http://example.com\nAI_KEY=secret"
        os.environ.clear()

        # Act & Assert
        with self.assertRaisesRegex(SystemExit, "No API key found"):
            main()

    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com'}, clear=True)
    def test_main_missing_api_key(self):
        # Arrange
        os.environ['AI_KEY'] = ''

        # Act & Assert
        with self.assertRaisesRegex(SystemExit, "No API key found"):
            main()

    @patch.dict(os.environ, {'AI_KEY': 'secret'}, clear=True)
    def test_main_missing_api_endpoint(self):
        # Arrange
        os.environ['AI_ENDPOINT'] = ''

        # Act & Assert
        with self.assertRaisesRegex(SystemExit, "No API endpoint found"):
            main()

if __name__ == '__main__':
    unittest.main()