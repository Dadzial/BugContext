import unittest
from unittest.mock import MagicMock, patch
from src.models.gemini_model import GeminiModel

class TestGeminiModel(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.api_key = "test_api_key"
        with patch('google.genai.Client'):
            self.model = GeminiModel(api_key=self.api_key)

    def test_analyze_logs_empty_input_raises_value_error(self):
        # Arrange
        logs = ""

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.model.analyze_logs(logs)
        
        self.assertEqual(str(context.exception), "Logs content cannot be empty.")

    @patch('src.models.gemini_model.GeminiModel.generate_response')
    def test_analyze_logs_returns_analysis(self, mock_generate_response):
        # Arrange
        logs = "ERROR: something went wrong"
        expected_analysis = "1. Błąd: Coś poszło nie tak. 2. Przyczyna: Nieznana. 3. Możliwa naprawa: Sprawdź logi."
        mock_generate_response.return_value = expected_analysis

        # Act
        result = self.model.analyze_logs(logs)

        # Assert
        self.assertEqual(result, expected_analysis)
        mock_generate_response.assert_called_once()
        # Verify if prompt contains logs
        args, _ = mock_generate_response.call_args
        self.assertIn(logs, args[0])

if __name__ == '__main__':
    unittest.main()
