import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_missing_env_variables(self, mock_getenv):
        mock_getenv.side_effect = [None, None]  # Mocking missing environment variables
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('http.request.urlopen')
    @patch('os.getenv')
    def test_main_http_error(self, mock_getenv, mock_urlopen):
        mock_getenv.return_value = "valid_key"
        mock_urlopen.side_effect = error.HTTPError('http://example.com', 404, 'Not Found', {}, None)
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_invalid_data_type(self, mock_getenv):
        mock_getenv.side_effect = ["not_a_number", "another_not_a_number"]  # Mocking invalid data type for key
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()