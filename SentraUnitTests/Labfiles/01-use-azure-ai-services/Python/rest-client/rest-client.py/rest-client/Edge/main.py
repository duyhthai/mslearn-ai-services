import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_with_valid_env_variables(self, mock_getenv):
        mock_getenv.return_value = "http://example.com/api"
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    @patch('os.getenv', return_value=None)
    def test_main_without_ai_endpoint(self, mock_getenv):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch('os.getenv', return_value="http://example.com/api")
    @patch('urllib.request.urlopen')
    def test_main_with_error_response(self, mock_urlopen):
        mock_urlopen.side_effect = error.URLError("Failed to reach server")
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()