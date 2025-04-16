import unittest
from app import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_redirects_to_login(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)

    def test_login_page_loads(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'LOGIN', response.data)

if __name__ == "__main__":
    unittest.main()
