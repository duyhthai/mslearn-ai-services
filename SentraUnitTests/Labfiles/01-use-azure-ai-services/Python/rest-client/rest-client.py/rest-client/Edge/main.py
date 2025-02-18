import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('dotenv.load_dotenv')
    def test_main_with_valid_environment_variables(self, mock_load_dotenv):
        # Arrange
        os.environ['AI_ENDPOINT'] = 'http://example.com'
        os.environ['AI_KEY'] = 'valid_key'

        # Mock the requests library
        with patch('http.client.HTTPSConnection') as mock_connection:
            mock_response = mock_connection.return_value.getresponse.return_value
            mock_response.status = 200
            mock_response.read.return_value = '{"result": "success"}'.encode()

            # Act
            main()

            # Assert
            mock_load_dotenv.assert_called_once()
            mock_connection.assert_called_once_with('example.com', 443)
            mock_connection.return_value.request.assert_called_once_with('GET', '/endpoint')

    @patch('dotenv.load_dotenv')
    def test_main_without_ai_endpoint(self, mock_load_dotenv):
        # Arrange
        del os.environ['AI_ENDPOINT']
        os.environ['AI_KEY'] = 'valid_key'

        # Act & Assert
        with self.assertRaises(KeyError):
            main()

    @patch('dotenv.load_dotenv')
    def test_main_without_ai_key(self, mock_load_dotenv):
        # Arrange
        os.environ['AI_ENDPOINT'] = 'http://example.com'
        del os.environ['AI_KEY']

        # Act & Assert
        with self.assertRaises(KeyError):
            main()

if __name__ == '__main__':
    unittest.main()