# Import necessary libraries
import unittest
from unittest.mock import patch, Mock
from io import StringIO
import sys

# Mock the required modules and functions
@patch('dotenv.load_dotenv')
@patch.dict(os.environ, {'AI_ENDPOINT': 'http://example.com', 'AI_KEY': '12345'})
class TestMain(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.old_stdout = sys.stdout
        self.new_stdout = StringIO()
        sys.stdout = self.new_stdout

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.old_stdout

    @patch('http.client.HTTPSConnection')
    def test_main_with_valid_input(self, mock_connection):
        # Arrange
        mock_response = Mock(status=200)
        mock_connection.return_value.getresponse.return_value = mock_response
        mock_connection.return_value.getresponse().read.return_value = '{"result": "success"}'

        # Act
        main()

        # Assert
        mock_connection.assert_called_once_with('example.com')
        mock_connection.return_value.request.assert_called_once_with('GET', '/?api_key=12345')
        self.assertEqual(self.new_stdout.getvalue(), 'Success\n')

if __name__ == '__main__':
    unittest.main()