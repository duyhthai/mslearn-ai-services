# Unit Tests for the given source code

import unittest
from unittest.mock import patch, MagicMock
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict(os.environ, {'AZURE_TEXT_ANALYTICS_ENDPOINT': '', 'AZURE_TEXT_ANALYTICS_KEY': ''})
    def test_main_empty_env_variables(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict(os.environ, {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'invalid_url', 'AZURE_TEXT_ANALYZICS_KEY': 'valid_key'})
    def test_main_invalid_endpoint(self):
        with self.assertRaises(Exception):
            main()

    @patch.dict(os.environ, {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'http://localhost:5000', 'AZURE_TEXT_ANALYZICS_KEY': ''})
    def test_main_empty_key(self):
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()