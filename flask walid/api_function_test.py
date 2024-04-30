import unittest
import requests

class TestAPIFunction(unittest.TestCase):

    def test_add_note_api(self):
        response = requests.post('http://localhost:5000/add', data=dict(title='Test Note', content='Test Content'))
        self.assertEqual(response.status_code, 200)  # Assuming API returns 200 on success

if __name__ == '__main__':
    unittest.main()
