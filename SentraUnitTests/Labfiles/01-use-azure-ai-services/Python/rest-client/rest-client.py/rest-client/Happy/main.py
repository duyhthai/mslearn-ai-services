import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_with_valid_env_vars(self, mock_getenv):
        mock_getenv.return_value = 'http://example.com/api'
        
        with self.assertRaises(SystemExit) as context:
            main()
        
        self.assertEqual(context.exception.code, 0)

    @patch('os.getenv')
    def test_main_without_ai_endpoint(self, mock_getenv):
        mock_getenv.side_effect = ['not_found', 'key']
        
        with self.assertRaises(SystemExit) as context:
            main()
        
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_without_ai_key(self, mock_getenv):
        mock_getenv.side_effect = ['endpoint', 'not_found']
        
        with self.assertRaises(SystemExit) as context:
            main()
        
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()