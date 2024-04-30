import unittest
from app import app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_content(self):
        response = self.app.get('/')
        self.assertIn(b'<h1>Note Taker</h1>', response.data)

    def test_add_note_form(self):
        response = self.app.get('/add')
        self.assertIn(b'<h1>Add Note</h1>', response.data)

if __name__ == '__main__':
    unittest.main()
