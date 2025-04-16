import unittest
from app import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_redirect(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_login_loads(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
