# Unit tests for negative scenarios in the given source code

class TestMainFunctionNegative:
    def test_missing_environment_variables(self):
        # Arrange
        original_environ = dict(os.environ)
        os.environ.clear()

        # Act & Assert
        with self.assertRaises(KeyError):
            main()

        # Cleanup
        os.environ.update(original_environ)

    def test_invalid_ai_endpoint_type(self):
        # Arrange
        original_environ = dict(os.environ)
        os.environ['AI_ENDPOINT'] = 'not_a_url'
        os.environ['AI_KEY'] = 'some_key'

        # Act & Assert
        with self.assertRaises(ValueError):
            main()

        # Cleanup
        os.environ.update(original_environ)

    def test_http_error_in_request(self):
        # Arrange
        original_environ = dict(os.environ)
        os.environ['AI_ENDPOINT'] = 'http://example.com/api'
        os.environ['AI_KEY'] = 'some_key'

        mock_response = Mock(status=404)
        mock_request.urlopen.side_effect = HTTPError(mock_response.url, mock_response.status, mock_response.reason, mock_response.headers, None)

        # Act & Assert
        with self.assertRaises(HTTPError):
            main()

        # Cleanup
        os.environ.update(original_environ)
        mock_request.urlopen.reset_mock()