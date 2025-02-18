import unittest
from unittest.mock import patch
from your_module import GetLanguage

class TestGetLanguage(unittest.TestCase):
    @patch.dict(os.environ, {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'http://localhost', 'AZURE_TEXT_ANALYZER_KEY': 'key'})
    def test_get_language_valid_text(self):
        text = "Hello world"
        expected_result = 'en'
        with patch('azure.ai.textanalytics.TextAnalyticsClient') as mock_client:
            mock_client.return_value.detect_languages.return_value.cognitive_model_versions = ['latest']
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

    @patch.dict(os.environ, {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'http://localhost', 'AZURE_TEXT_ANALYZER_KEY': 'key'})
    def test_get_language_empty_text(self):
        text = ""
        expected_result = None
        with patch('azure.ai.textanalytics.TextAnalyticsClient') as mock_client:
            mock_client.return_value.detect_languages.return_value.cognitive_model_versions = ['latest']
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

    @patch.dict(os.environ, {'AZURE_TEXT_ANALYTICS_ENDPOINT': 'http://localhost', 'AZURE_TEXT_ANALYZER_KEY': 'key'})
    def test_get_language_none_text(self):
        text = None
        expected_result = None
        with patch('azure.ai.textanalytics.TextAnalyticsClient') as mock_client:
            mock_client.return_value.detect_languages.return_value.cognitive_model_versions = ['latest']
            result = GetLanguage(text)
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()