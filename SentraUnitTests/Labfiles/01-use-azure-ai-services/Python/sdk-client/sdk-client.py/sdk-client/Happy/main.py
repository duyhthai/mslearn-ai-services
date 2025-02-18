import unittest
from unittest.mock import patch, Mock
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):
    @patch('os.getenv')
    def test_main_with_valid_inputs(self, mock_getenv):
        # Arrange
        mock_getenv.return_value = "https://fakeendpoint.cognitiveservices.azure.com"
        mock_text_analytics_client = Mock(spec=TextAnalyticsClient)
        
        with patch('azure.ai.textanalytics.TextAnalyticsClient', return_value=mock_text_analytics_client) as mock_client_class:
            # Act
            main()
            
            # Assert
            mock_getenv.assert_called_once_with('AZURE_ENDPOINT')
            mock_getenv.assert_called_once_with('AZURE_KEY')
            mock_client_class.assert_called_once_with(endpoint="https://fakeendpoint.cognitiveservices.azure.com", credential=None)

if __name__ == '__main__':
    unittest.main()