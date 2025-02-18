import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_with_missing_env_vars(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('http.request.urlopen')
    @patch('os.getenv')
    def test_main_with_http_error(self, mock_getenv, mock_request):
        mock_getenv.return_value = "test_key"
        mock_request.side_effect = error.HTTPError("URL", 404, "Not Found", {}, None)
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_with_invalid_api_key(self, mock_getenv):
        mock_getenv.return_value = "invalid_key"
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()