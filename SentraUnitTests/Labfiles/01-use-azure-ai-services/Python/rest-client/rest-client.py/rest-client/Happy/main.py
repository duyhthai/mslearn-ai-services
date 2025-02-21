import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name where 'main' is defined

class TestMain(unittest.TestCase):
    
    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'testkey'})
    def test_main_success(self):
        with patch('http.client.HTTPConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = '{"result": "success"}'
            
            main()
            
            mock_connection.assert_called_once_with('example.com')
            mock_connection.return_value.request.assert_called_once_with('GET', '/?api_key=testkey')

    @patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_missing_env_vars(self):
        with self.assertRaises(ValueError):
            main()

    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'testkey'})
    @patch('http.client.HTTPConnection')
    def test_main_http_error(self, mock_connection):
        mock_response = mock_connection.return_value.getresponse.return_value
        mock_response.status = 500
        
        with self.assertRaises(Exception) as context:
            main()
        
        self.assertIn('HTTP Error 500', str(context.exception))

if __name__ == '__main__':
    unittest.main()