import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_missing_env_variables(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_empty_env_variables(self):
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('http.request.urlopen')
    def test_http_request_error(self, mock_urlopen):
        mock_urlopen.side_effect = error.URLError("Test Error")
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()