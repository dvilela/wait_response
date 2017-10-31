#!/usr/bin/env python3

import unittest

import responses

from wait_response import wait_response_status


class TestWaitResponse(unittest.TestCase):
    def test_wait_response_status_until_max_attempts(self):
        result = wait_response_status('http://localhost:8080/someWrongUrl', 2, 1, 'UP')
        self.assertEqual(result, 1)

    @responses.activate
    def test_wait_response_status_up(self):
        responses.add(responses.GET, 'http://localhost:8080/health',
                      json={'status': 'UP'}, status=200)
        result = wait_response_status('http://localhost:8080/health', 2, 1, 'UP')
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
