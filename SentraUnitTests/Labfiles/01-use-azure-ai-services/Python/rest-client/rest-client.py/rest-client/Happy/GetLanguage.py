import unittest
from unittest.mock import patch
from your_module import GetLanguage  # Replace 'your_module' with the actual module name

class TestGetLanguage(unittest.TestCase):
    @patch.dict(os.environ, {'LANG': 'en_US.UTF-8'})
    def test_get_language_valid_input(self):
        text = "Hello, world!"
        result = GetLanguage(text)
        self.assertEqual(result, 'English')

    @patch.dict(os.environ, {'LANG': 'fr_FR.UTF-8'})
    def test_get_language_french_input(self):
        text = "Bonjour le monde!"
        result = GetLanguage(text)
        self.assertEqual(result, 'French')

    @patch.dict(os.environ, {'LANG': 'es_ES.UTF-8'})
    def test_get_language_spanish_input(self):
        text = "Hola mundo!"
        result = GetLanguage(text)
        self.assertEqual(result, 'Spanish')

if __name__ == '__main__':
    unittest.main()