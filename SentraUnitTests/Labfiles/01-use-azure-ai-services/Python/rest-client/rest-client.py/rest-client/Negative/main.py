import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_main_missing_ai_endpoint(self, mock_getenv):
        mock_getenv.side_effect = lambda key: None if key == 'AI_ENDPOINT' else 'some_value'
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_missing_ai_key(self, mock_getenv):
        mock_getenv.side_effect = lambda key: 'some_value' if key == 'AI_KEY' else None
        with self.assertRaises(SystemExit) as context:
            main()
        self.assertEqual(context.exception.code, 1)

    @patch('os.getenv')
    def test_main_invalid_ai_endpoint(self, mock_getenv):
        mock_getenv.return_value = 'invalid_url'
        with self.assertRaises(ValueError) as context:
            main()
        self.assertIn("Invalid URL", str(context.exception))

if __name__ == '__main__':
    unittest.main()