import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_note(self):
        response = self.app.post('/add', data=dict(title='Test Note', content='Test Content'))
        self.assertEqual(response.status_code, 302)  # Redirects to index on successful addition

    def test_delete_note(self):
        response = self.app.post('/delete/1')  # Replace '1' with an actual note ID
        self.assertEqual(response.status_code, 302)  # Redirects to index on successful deletion

if __name__ == '__main__':
    unittest.main()
