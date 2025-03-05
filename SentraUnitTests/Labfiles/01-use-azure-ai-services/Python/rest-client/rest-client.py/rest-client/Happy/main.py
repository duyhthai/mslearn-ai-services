import unittest
from unittest.mock import patch, mock_open
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com/api', 'AI_KEY': '12345'})
    def test_main_with_valid_env_variables(self):
        with patch('http.request.urlopen') as mock_request:
            mock_request.return_value.read.return_value = '{"response": "success"}'
            main()
            mock_request.assert_called_once_with(
                'http://example.com/api',
                headers={'Authorization': 'Bearer 12345'},
                data=None,
                method='GET'
            )

    @patch.dict('os.environ', {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_with_empty_env_variables(self):
        with self.assertRaisesRegex(SystemExit, 'System exit'):
            main()

    @patch.dict('os.environ', {'AI_ENDPOINT': None, 'AI_KEY': None})
    def test_main_with_none_env_variables(self):
        with self.assertRaisesRegex(SystemExit, 'System exit'):
            main()

if __name__ == '__main__':
    unittest.main()