import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get_language_success(self, mock_urlopen):
        mock_response = type('MockResponse', (), {'read': lambda x: '{"language": "English"}'.encode()})
        mock_urlopen.return_value = mock_response
        
        result = GetLanguage("Hello World")
        
        self.assertEqual(result, "English")

    @patch('urllib.request.urlopen')
    def test_get_language_http_error(self, mock_urlopen):
        mock_urlopen.side_effect = error.HTTPError(url=None, code=404, msg='Not Found', hdrs={}, fp=None)
        
        with self.assertRaises(error.HTTPError) as context:
            GetLanguage("Hello World")
        
        self.assertEqual(context.exception.code, 404)

    @patch('urllib.request.urlopen')
    def test_get_language_invalid_json(self, mock_urlopen):
        mock_response = type('MockResponse', (), {'read': lambda x: b'invalid json'})
        mock_urlopen.return_value = mock_response
        
        with self.assertRaises(ValueError) as context:
            GetLanguage("Hello World")
        
        self.assertIn('Expecting property name enclosed in double quotes', str(context.exception))

if __name__ == '__main__':
    unittest.main()