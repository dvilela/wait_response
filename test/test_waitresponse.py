import unittest

import responses

import waitresponse
from waitresponse import waitresponse

class TestWaitresponse(unittest.TestCase):

    def test_waitresponse_until_max_attempts(self):
        result = waitresponse('http://localhost:8080/someWrongUrl', 2, 1, 'UP')
        self.assertEqual(result, 1)

    @responses.activate
    def test_waitresponse_ok(self):
        responses.add(responses.GET, 'http://localhost:8080/health',
                  json={'status': 'UP'}, status=200)
        result = waitresponse('http://localhost:8080/health', 2, 1, 'UP')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
