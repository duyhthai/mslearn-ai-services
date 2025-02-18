import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    
    @patch('builtins.open')
    def test_load_dotenv_failure(self, mock_open):
        mock_open.side_effect = FileNotFoundError("dotenv file not found")
        with self.assertRaises(FileNotFoundError):
            main()

    @patch.dict(os.environ, {'AI_KEY': ''})
    def test_ai_key_empty(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict(os.environ, {'AI_ENDPOINT': ''})
    def test_ai_endpoint_empty(self):
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()