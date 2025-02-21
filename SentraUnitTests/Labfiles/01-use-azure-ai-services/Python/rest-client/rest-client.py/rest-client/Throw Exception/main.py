import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    @patch('dotenv.load_dotenv')
    def test_main_missing_ai_endpoint(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_missing_ai_key(self, mock_getenv):
        mock_getenv.side_effect = lambda key: None if key == 'AI_KEY' else 'http://example.com'
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('urllib.request.urlopen')
    @patch('os.getenv')
    def test_main_http_error(self, mock_getenv, mock_urlopen):
        mock_getenv.side_effect = lambda key: 'http://example.com' if key == 'AI_ENDPOINT' else 'key'
        mock_urlopen.side_effect = error.HTTPError('', 404, '', {}, None)
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()