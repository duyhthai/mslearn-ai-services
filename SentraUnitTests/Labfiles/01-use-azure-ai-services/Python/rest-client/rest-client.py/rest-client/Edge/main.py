import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict('os.environ', {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_empty_env_vars(self):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'testkey'})
    def test_main_valid_env_vars(self):
        with self.patch('http.request.urlopen') as mock_request:
            mock_response = mock_request.return_value
            mock_response.read.return_value = b'success'
            main()
            mock_request.assert_called_once_with(
                url='http://example.com',
                headers={'Authorization': 'Bearer testkey'}
            )

    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'testkey'})
    def test_main_http_error(self):
        with self.patch('http.request.urlopen') as mock_request:
            mock_request.side_effect = error.HTTPError('http://example.com', 500, 'Internal Server Error', {}, None)
            with self.assertRaisesRegex(SystemExit, 'HTTP Error 500'):
                main()

if __name__ == '__main__':
    unittest.main()