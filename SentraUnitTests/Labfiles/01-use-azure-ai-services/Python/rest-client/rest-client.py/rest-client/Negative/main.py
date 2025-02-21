import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name where main is defined

class TestMain(unittest.TestCase):
    @patch('os.getenv')
    def test_missing_env_vars(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('http.request.urlopen')
    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'testkey'})
    def test_http_error(self, mock_urlopen):
        mock_urlopen.side_effect = error.HTTPError(None, None, "HTTP Error", {}, None)
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('http.request.urlopen')
    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'testkey'})
    def test_other_error(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Other error")
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()