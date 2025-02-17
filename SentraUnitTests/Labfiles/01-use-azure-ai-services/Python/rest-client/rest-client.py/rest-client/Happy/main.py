import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_with_valid_env_vars(self, mock_getenv):
        mock_getenv.return_value = 'valid_ai_endpoint'
        main()
        # Add assertions to check if the global variables are set correctly
        self.assertEqual(ai_endpoint, 'valid_ai_endpoint')

    @patch('os.getenv')
    def test_main_with_missing_env_vars(self, mock_getenv):
        mock_getenv.side_effect = [None, None]  # Simulate missing env vars
        with self.assertRaises(SystemExit) as context:
            main()
        # Add assertion to check if SystemExit is raised
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_with_invalid_env_var_type(self, mock_getenv):
        mock_getenv.return_value = 123  # Simulate invalid type for ai_endpoint
        with self.assertRaises(SystemExit) as context:
            main()
        # Add assertion to check if SystemExit is raised
        self.assertEqual(context.exception.code, 1)

if __name__ == '__main__':
    unittest.main()