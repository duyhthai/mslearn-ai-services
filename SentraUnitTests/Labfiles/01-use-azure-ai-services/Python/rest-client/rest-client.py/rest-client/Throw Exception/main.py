import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    @patch('os.getenv')
    def test_main_no_env_vars(self, mock_getenv):
        mock_getenv.side_effect = [None] * 2  # Mocking both ai_endpoint and ai_key as None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('http.request.urlopen')
    @patch('os.getenv')
    def test_main_request_exception(self, mock_getenv, mock_urlopen):
        mock_getenv.return_value = "some_value"
        mock_urlopen.side_effect = error.URLError("Test Error")
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_invalid_url(self, mock_getenv):
        mock_getenv.return_value = "invalid://url"
        with self.assertRaises(ValueError) as context:
            main()
        self.assertIn("Invalid URL", str(context.exception))

if __name__ == '__main__':
    unittest.main()