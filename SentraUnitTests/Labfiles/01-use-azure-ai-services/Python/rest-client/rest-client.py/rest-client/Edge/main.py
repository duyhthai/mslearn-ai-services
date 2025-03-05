import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict('os.environ', {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_empty_env(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com/api', 'AI_KEY': 'abc123'})
    def test_main_valid_env(self):
        with patch.object(http.client, 'HTTPConnection') as mock_connection:
            main()
            mock_connection.assert_called_once_with('example.com')

    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com/api', 'AI_KEY': None})
    def test_main_none_key(self):
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()