import unittest
from unittest.mock import patch, MagicMock
from your_module import main  # Replace 'your_module' with the actual module name

class TestMain(unittest.TestCase):

    @patch('dotenv.load_dotenv')
    def test_main_loads_environment_variables(self, mock_load_dotenv):
        main()
        mock_load_dotenv.assert_called_once()

    @patch.dict(os.environ, {'AI_ENDPOINT': '', 'AI_KEY': ''})
    def test_main_handles_empty_environment_variables(self):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

    @patch.dict(os.environ, {'AI_ENDPOINT': None, 'AI_KEY': None})
    def test_main_handles_none_environment_variables(self):
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()