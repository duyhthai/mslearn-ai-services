import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict('os.environ', {'AZURE_TEXT_ANALYTICS_ENDPOINT': '', 'AZURE_TEXT_ANALYTICS_KEY': ''})
    def test_main_with_empty_env_vars(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict('os.environ', {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'https://example.com', 'AZURE_TEXT_ANALYTICS_KEY': ''})
    def test_main_with_missing_key(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict('os.environ', {'AZURE_TEXT_ANALYTICS_ENDPOINT': '', 'AZURE_TEXT_ANALYTICS_KEY': 'key'})
    def test_main_with_missing_endpoint(self):
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()