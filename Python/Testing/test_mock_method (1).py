import unittest
import json
from unittest.mock import patch, MagicMock
from method import get_weather

class GetWetherTest(unittest.TestCase):
    
    @patch('method.requests')
    def test_bad(self, request_mock):
        with open('wether_response.json', 'r') as f:
            body = json.load(f)
        requests_response_mock = MagicMock()
        requests_response_mock.status_code = 200
        requests_response_mock.json.return_value = body
        request_mock.get.return_value = requests_response_mock
        self.assertEqual('Bad', get_weather('12345'))

    @patch('method.requests')
    def test_success(self, request_mock):
        request_response_mock = MagicMock()
        request_response_mock.status_code = 200
        request_response_mock.json.return_value = {'main': {'temp': 23}}
        request_mock.get.return_value = request_response_mock
        self.assertEqual('Good', get_weather('haha'))

    @patch('method.requests')
    def test_failed(self, request_mock):
        request_response_mock = MagicMock()
        request_response_mock.status_code = 404
        request_mock.get.return_value = request_response_mock
        with self.assertRaises(RuntimeError):
            get_weather('12345')



        
        
