import unittest
from unittest.mock import patch, mock_open
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('your_module.load_dotenv')  # Replace 'your_module' with the actual module name
    def test_get_language_success(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        text = "Hello, world!"
        response_text = '{"language": "English"}'
        
        with patch('urllib.request.urlopen', return_value=mock_open(read_data=response_text).return_value) as mock_urlopen:
            result = GetLanguage(text)
            self.assertEqual(result, 'English')

    @patch('your_module.load_dotenv')  # Replace 'your_module' with the actual module name
    def test_get_language_error(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        text = "Hello, world!"
        
        with patch('urllib.request.urlopen', side_effect=error.URLError("Test Error")) as mock_urlopen:
            with self.assertRaises(error.URLError):
                GetLanguage(text)

    @patch('your_module.load_dotenv')  # Replace 'your_module' with the actual module name
    def test_get_language_invalid_response(self, mock_load_dotenv):
        mock_load_dotenv.return_value = None
        text = "Hello, world!"
        response_text = '{"invalid": "data"}'
        
        with patch('urllib.request.urlopen', return_value=mock_open(read_data=response_text).return_value) as mock_urlopen:
            with self.assertRaises(ValueError):
                GetLanguage(text)

if __name__ == '__main__':
    unittest.main()