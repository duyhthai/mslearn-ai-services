import unittest
from unittest.mock import patch, MagicMock
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    @patch('azure.ai.textanalytics.TextAnalyticsClient')
    def test_get_language_exception(self, mock_client):
        mock_client.return_value.detect_languages.side_effect = Exception("Mocked Exception")
        
        with self.assertRaises(Exception) as context:
            GetLanguage("test text")

        self.assertTrue("Mocked Exception" in str(context.exception))

if __name__ == '__main__':
    unittest.main()