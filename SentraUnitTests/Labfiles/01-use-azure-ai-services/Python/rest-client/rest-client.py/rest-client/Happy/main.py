import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name where main is defined

class TestMain(unittest.TestCase):
    @patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': 'test_key'})
    def test_main_with_valid_inputs(self):
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.read.return_value = '{"result": "success"}'
            
            main()
            
            mock_connection.assert_called_once_with('example.com')
            mock_connection.return_value.request.assert_called_once_with('GET', '/api/main?api_key=test_key')

if __name__ == '__main__':
    unittest.main()