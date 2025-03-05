import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    
    @patch('os.environ.get')
    def test_main_missing_env_vars(self, mock_get):
        mock_get.return_value = None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('urllib.request.urlopen')
    @patch('os.environ.get')
    def test_main_http_error(self, mock_get, mock_urlopen):
        mock_get.side_effect = lambda key: 'http://example.com' if key == 'AI_ENDPOINT' else 'key'
        mock_urlopen.side_effect = error.HTTPError(None, 400, None, None, None)
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('urllib.parse.urlencode')
    @patch('urllib.request.urlopen')
    @patch('os.environ.get')
    def test_main_request_error(self, mock_get, mock_urlopen, mock_urlencode):
        mock_get.side_effect = lambda key: 'http://example.com' if key == 'AI_ENDPOINT' else 'key'
        mock_urlopen.side_effect = Exception("Request failed")
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()