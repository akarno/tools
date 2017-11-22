
import unittest
from unittest.mock import patch

class TestClient(unittest.TestCase):
    def setUp(self):
        self.vars_client = VarsClient()

    @patch('pyvars.vars_client.VarsClient.get')
    @patch('requests.post')
    def test_update_retry_works_eventually(self, mock_post, mock_get):
        mock_get.side_effect = [
            VarsResponse(),
            VarsResponse()]
        mock_post.side_effect = [
            requests.ConnectionError('Test error'),
            MagicMock(status_code=200, headers={'content-type':"application/json"},
                             text=json.dumps({'status':True}))
        ]
        response = self.vars_client.update('test', '0')
        self.assertEqual(response, response)
