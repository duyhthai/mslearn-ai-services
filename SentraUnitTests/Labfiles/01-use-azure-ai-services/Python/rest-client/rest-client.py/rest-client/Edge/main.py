import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_with_valid_environment_variables(self, mock_getenv):
        mock_getenv.side_effect = ['http://example.com', 'valid_api_key']
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)

    @patch('os.getenv')
    def test_main_with_missing_ai_endpoint(self, mock_getenv):
        mock_getenv.return_value = None
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch('os.getenv')
    def test_main_with_missing_ai_key(self, mock_getenv):
        mock_getenv.side_effect = ['http://example.com', None]
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()