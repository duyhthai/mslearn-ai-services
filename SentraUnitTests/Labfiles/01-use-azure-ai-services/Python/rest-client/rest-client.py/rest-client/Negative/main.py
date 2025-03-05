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

    @patch.dict('os.environ', {'AI_ENDPOINT': 'invalid_url', 'AI_KEY': 'key'})
    def test_main_invalid_url(self):
        with self.assertRaises(error.URLError):
            main()

if __name__ == '__main__':
    unittest.main()