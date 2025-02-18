import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict('os.environ', {'AZURE_TEXT_ANALYTICS_ENDPOINT': '', 'AZURE_TEXT_ANALYTICS_KEY': ''})
    def test_main_missing_env_vars(self):
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("Environment variables AZURE_TEXT_ANALYTICS_ENDPOINT and AZURE_TEXT_ANALYTICS_KEY must be set", str(context.exception))

    @patch.dict('os.environ', {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'http://example.com', 'AZURE_TEXT_ANALYTICS_KEY': None})
    def test_main_invalid_key(self):
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("Environment variable AZURE_TEXT_ANALYTICS_KEY cannot be None", str(context.exception))

    @patch.dict('os.environ', {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'http://example.com', 'AZURE_TEXT_ANALYTICS_KEY': 'invalid-key'})
    @patch('azure.ai.textanalytics.TextAnalyticsClient')
    def test_main_auth_failure(self, mock_client):
        mock_client.side_effect = Exception("Authentication failed")
        with self.assertRaises(Exception) as context:
            main()
        self.assertIn("Authentication failed", str(context.exception))

if __name__ == '__main__':
    unittest.main()