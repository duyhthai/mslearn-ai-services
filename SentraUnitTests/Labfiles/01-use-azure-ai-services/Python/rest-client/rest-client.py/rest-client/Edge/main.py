import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    
    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com/api', 'AI_KEY': 'abc123'})
    def test_main_with_valid_env_variables(self):
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = b'{"result": "success"}'
            main()
            mock_connection.assert_called_once_with('example.com')
            mock_connection.return_value.request.assert_called_once_with('GET', '/api')

    @patch.dict('os.environ', {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_with_empty_env_variables(self):
        with self.assertRaises(SystemExit):
            main()

    @patch.dict('os.environ', {'AI_ENDPOINT': None, 'AI_KEY': None})
    def test_main_with_none_env_variables(self):
        with self.assertRaises(SystemExit):
            main()

if __name__ == '__main__':
    unittest.main()