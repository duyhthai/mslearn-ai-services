import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('dotenv.load_dotenv')
    def test_main_loads_dotenv(self, mock_load_dotenv):
        main()
        mock_load_dotenv.assert_called_once()

    @patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''})
    @patch('http.client.HTTPConnection.request')
    def test_main_raises_exception_on_empty_ai_endpoint(self, mock_request):
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("AI_ENDPOINT is required", str(context.exception))

    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': ''})
    @patch('http.client.HTTPConnection.request')
    def test_main_raises_exception_on_empty_ai_key(self, mock_request):
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("AI_KEY is required", str(context.exception))

if __name__ == '__main__':
    unittest.main()