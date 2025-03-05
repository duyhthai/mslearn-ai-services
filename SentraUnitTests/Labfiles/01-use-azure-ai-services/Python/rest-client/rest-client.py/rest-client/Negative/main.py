import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict('os.environ', {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_empty_env_variables(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': None})
    def test_main_none_ai_key(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict('os.environ', {'AI_ENDPOINT': None, 'AI_KEY': 'secret_key'})
    def test_main_none_ai_endpoint(self):
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()