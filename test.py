import unittest
from unittest.mock import mock_open, patch
from check_json_file import check_json_file


class UnitTestForFunction(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(UnitTestForFunction, self).__init__(*args, **kwargs)
        self.json_file_path = 'C:/Users/szczy/Desktop/STUDIA/dodat/Remitly/data.json'

    # Test for valid JSON data with a resource that is not a single asterisk
    def test_valid_json(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {"Statement": [{"Resource": "123"}]}}')):
            result = check_json_file(self.json_file_path)
            self.assertTrue(result)

    # Test for JSON data with a resource that contains a single asterisk
    def test_json_with_single_asterisk(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {"Statement": [{"Resource": "*"}]}}')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for JSON data with invalid format
    def test_invalid_json_format(self):
        with patch('builtins.open', mock_open(read_data='{invalid_json')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for handling file not found error
    def test_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for an empty JSON file
    def test_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for JSON data missing the 'PolicyDocument' key
    def test_no_policy_document_key(self):
        with patch('builtins.open', mock_open(read_data='{}')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for JSON data missing the 'Statement' key
    def test_no_statement_key(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {}}')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for JSON data missing the 'Resource' key
    def test_no_resource_key(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {"Statement": [{}]}}')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for JSON data with a resource that is not a string
    def test_resource_not_string(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {"Statement": [{"Resource": 123}]}}')):
            result = check_json_file(self.json_file_path)
            self.assertTrue(result)

    # Test for JSON data with multiple statements including one with a single asterisk resource
    def test_multiple_statements(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {"Statement": [{"Resource": "123"}, {"Resource": "*"}]}}')):
            result = check_json_file(self.json_file_path)
            self.assertFalse(result)

    # Test for JSON data with resource that contain two asterisk
    def test_multiple_asterisk(self):
        with patch('builtins.open', mock_open(read_data='{"PolicyDocument": {"Statement": [{"Resource": "**"}]}}')):
            result = check_json_file(self.json_file_path)
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
