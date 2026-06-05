import unittest
from unittest.mock import patch, MagicMock
from src.app import app

class TestGeminiController(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.app = app.test_client()
        self.app.testing = True

    @patch('src.controllers.gemini_controller.gemini_model.analyze_logs')
    def test_analyze_success(self, mock_analyze):
        # Arrange
        mock_analyze.return_value = "Mocked Analysis"
        payload = {'logs': 'test logs'}

        # Act
        response = self.app.post('/api/analyze', json=payload)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'analysis': 'Mocked Analysis'})
        mock_analyze.assert_called_once_with('test logs')

    def test_analyze_no_logs_provided(self):
        # Arrange
        payload = {}

        # Act
        response = self.app.post('/api/analyze', json=payload)

        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertIn('No logs provided', response.get_json()['error'])

    @patch('src.controllers.gemini_controller.gemini_model.analyze_logs')
    def test_analyze_internal_error(self, mock_analyze):
        # Arrange
        mock_analyze.side_effect = Exception("Internal error")
        payload = {'logs': 'test logs'}

        # Act
        response = self.app.post('/api/analyze', json=payload)

        # Assert
        self.assertEqual(response.status_code, 500)
        self.assertIn('Internal error', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()
