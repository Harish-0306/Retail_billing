import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def test_home_redirect(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()