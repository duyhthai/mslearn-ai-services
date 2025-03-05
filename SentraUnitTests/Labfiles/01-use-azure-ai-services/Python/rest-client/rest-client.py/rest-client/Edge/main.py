import unittest
from unittest.mock import patch
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch.dict('os.environ', {'AI_ENDPOINT': 'http://example.com/api/v1', 'AI_KEY': 'testkey'})
    def test_main_with_valid_env_variables(self):
        # Arrange
        expected_output = "Expected Output"  # Replace with the actual expected output

        # Act
        result = main()

        # Assert
        self.assertEqual(result, expected_output)

    @patch.dict('os.environ', {})
    def test_main_without_env_variables(self):
        # Arrange

        # Act
        with self.assertRaises(KeyError):
            main()

    @patch.dict('os.environ', {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_with_empty_env_variables(self):
        # Arrange

        # Act
        with self.assertRaises(ValueError):
            main()

if __name__ == '__main__':
    unittest.main()