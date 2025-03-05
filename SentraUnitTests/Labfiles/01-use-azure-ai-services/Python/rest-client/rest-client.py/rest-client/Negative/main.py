import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_with_empty_env_vars(self):
        with self.assertRaises(ValueError) as context:
            main()
        self.assertIn('AI_ENDPOINT and AI_KEY must be set', str(context.exception))

    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': None})
    def test_main_with_null_ai_key(self):
        with self.assertRaises(ValueError) as context:
            main()
        self.assertIn('AI_KEY cannot be None', str(context.exception))

    @patch.dict(os.environ, {'AI_ENDPOINT': None, 'AI_KEY': '12345'})
    def test_main_with_null_ai_endpoint(self):
        with self.assertRaises(ValueError) as context:
            main()
        self.assertIn('AI_ENDPOINT cannot be None', str(context.exception))

if __name__ == '__main__':
    unittest.main()