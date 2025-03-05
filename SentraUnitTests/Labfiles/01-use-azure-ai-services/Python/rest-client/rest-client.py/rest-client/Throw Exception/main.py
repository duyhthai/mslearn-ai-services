import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name where main function is defined

class TestMainFunction(unittest.TestCase):
    
    @patch('dotenv.load_dotenv')
    def test_main_without_ai_endpoint(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        os.environ['AI_KEY'] = 'some_key'
        with self.assertRaises(KeyError):
            main()

    @patch('dotenv.load_dotenv')
    def test_main_without_ai_key(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        os.environ['AI_ENDPOINT'] = 'http://example.com'
        with self.assertRaises(KeyError):
            main()

    @patch('os.getenv')
    @patch('http.request.urlopen')
    def test_main_with_http_error(self, mock_open_url, mock_getenv):
        mock_getenv.side_effect = lambda key: {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'some_key'}[key]
        mock_open_url.side_effect = error.URLError("Failed to connect")
        with self.assertRaises(error.URLError):
            main()

if __name__ == '__main__':
    unittest.main()