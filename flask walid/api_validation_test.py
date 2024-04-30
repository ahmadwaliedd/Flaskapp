import unittest
from app import app

class TestAPIValidation(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_note_validation(self):
        response = self.app.post('/add', data=dict(title='', content='Test Content'))
        self.assertEqual(response.status_code, 200)  # Should return 200 if validation fails

if __name__ == '__main__':
    unittest.main()
