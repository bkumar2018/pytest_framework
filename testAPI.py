import unittest
import requests

class APITestCase(unittest.TestCase):
    base_url = 'https://api.example.com'

    def test_get_request(self):
        response= requests.get(self.base_url+'/endpoint')

        self.assertIn('key', response.json())

    def test_post_request(self):
        payload = {'key': 'value'}
        response = requests.post(self.base_url+'/endpoint', json=payload)

        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
