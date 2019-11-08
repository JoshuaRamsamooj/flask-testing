import unittest
from app import create_app
import json


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app_ctx = self.app.app_context()
        self.app_ctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_ctx.pop()

    def test_home(self):
        response = self.client.get('/')
        response_data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], True)

    def test_greet(self):
        response = self.client.get('/greet/joshua')
        response_data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], True)
        self.assertEqual(response_data['greeting'], 'Hello joshua')

    def test_login(self):
        obj = {
            'name': 'joshua'
        }
        response = self.client.post('/login',
                                    json=obj)
        response_data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], True)
        self.assertEqual(response_data['name'], 'joshua')


