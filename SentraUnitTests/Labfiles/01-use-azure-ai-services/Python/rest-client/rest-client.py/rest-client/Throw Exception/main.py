import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name where main function resides

class TestMainFunction(unittest.TestCase):

    @patch('os.getenv')
    def test_main_raises_exception_when_ai_endpoint_is_none(self, mock_getenv):
        mock_getenv.side_effect = [None, 'key']
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("AI_ENDPOINT environment variable is missing", str(context.exception))

    @patch('os.getenv')
    def test_main_raises_exception_when_ai_key_is_none(self, mock_getenv):
        mock_getenv.side_effect = ['endpoint', None]
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("AI_KEY environment variable is missing", str(context.exception))

    @patch('os.getenv')
    def test_main_handles_valid_environment_variables(self, mock_getenv):
        mock_getenv.side_effect = ['endpoint', 'key']
        try:
            main()
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")

if __name__ == '__main__':
    unittest.main()