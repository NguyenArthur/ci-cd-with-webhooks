import unittest
from src.app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")

    def test_add_item(self):
        # Test adding an item
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        if response.text.find("Test Item") == -1:
            self.fail("Item not found in response")

    def test_delete_item(self):
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        
    def test_update_item(self):
        response = self.app.post('/add', data=dict(item="New Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        if response.text.find("New Test Item") == -1:
            self.fail("Item not found in response")
        response = self.app.post('/update/0', data=dict(new_item="Test Item updated"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        if response.text.find("Test Item updated") == -1:
            self.fail("Item not found in response")

if __name__ == '__main__':
    unittest.main()

