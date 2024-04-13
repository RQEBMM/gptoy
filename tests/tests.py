import unittest
from unittest.mock import patch
from spirit import ask 

class TestAskFunction(unittest.TestCase):

    @patch('requests.post')
    def test_ask_success(self, mock_post):
        # Mocking successful response
        mock_post.return_value.json.return_value = {"choices": [{"text": "Generated text"}]}
        result = ask("Prompt")
        self.assertEqual(result, "Generated text")

    @patch('requests.post')
    def test_ask_failure(self, mock_post):
        # Mocking failed response
        mock_post.side_effect = requests.exceptions.RequestException("Mocked exception")
        result = ask("Prompt")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
