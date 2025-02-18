import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('builtins.open')
    def test_main_with_valid_env(self, mock_open):
        mock_open.return_value = mock_open(read_data='AI_ENDPOINT=http://example.com\nAI_KEY=secret').return_value
        with patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''}):
            main()
            mock_open.assert_called_once_with('.env', 'r')
            self.assertEqual(os.environ['AI_ENDPOINT'], 'http://example.com')
            self.assertEqual(os.environ['AI_KEY'], 'secret')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_main_without_env_file(self, mock_open):
        with patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''}):
            main()
            mock_open.assert_called_once_with('.env', 'r')
            self.assertNotIn('AI_ENDPOINT', os.environ)
            self.assertNotIn('AI_KEY', os.environ)

    @patch('os.environ.get', return_value=None)
    def test_main_with_missing_env_vars(self, mock_get):
        with patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''}):
            main()
            self.assertNotIn('AI_ENDPOINT', os.environ)
            self.assertNotIn('AI_KEY', os.environ)

if __name__ == '__main__':
    unittest.main()