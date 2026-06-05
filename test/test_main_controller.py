import unittest
from src.app import app

class TestMainController(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.app = app.test_client()
        self.app.testing = True

    def test_health_endpoint(self):
        # Arrange
        # (Nothing special to arrange)

        # Act
        response = self.app.get('/api/health')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})

    def test_index_page(self):
        # Arrange
        # (Nothing special to arrange)

        # Act
        response = self.app.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        # Check if it returns HTML (index.html)
        self.assertIn(b'<!DOCTYPE html>', response.data)

if __name__ == '__main__':
    unittest.main()
