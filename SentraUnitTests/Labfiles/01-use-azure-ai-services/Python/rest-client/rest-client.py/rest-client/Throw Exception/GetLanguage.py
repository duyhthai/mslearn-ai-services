import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    @patch('os.environ')
    def test_get_language_no_env_var(self, mock_environ):
        mock_environ.get.return_value = None
        with self.assertRaises(EnvironmentError):
            GetLanguage("test text")

    @patch('urllib.request.urlopen')
    def test_get_language_http_error(self, mock_urlopen):
        mock_response = type('MockResponse', (), {'getcode': lambda x: 500})
        mock_urlopen.side_effect = error.HTTPError('http://example.com', 500, 'Internal Server Error', {}, None)
        with self.assertRaises(Exception) as context:
            GetLanguage("test text")
        self.assertIn('HTTP Error 500:', str(context.exception))

    @patch('urllib.parse.urlencode')
    @patch('urllib.request.urlopen')
    def test_get_language_success(self, mock_urlopen, mock_urlencode):
        mock_data = b'some data'
        mock_response = type('MockResponse', (), {'read': lambda x: mock_data})
        mock_urlopen.return_value = mock_response
        result = GetLanguage("test text")
        self.assertEqual(result, mock_data.decode())

if __name__ == '__main__':
    unittest.main()