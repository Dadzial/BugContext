import os
from google import genai
from google.genai.errors import APIError
from src.config import API_KEY

class GeminiModel:
    def __init__(self, model_name: str = "gemini-3.5-flash", api_key: str = API_KEY):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("API key missing. Set API_KEY in src/config.py or GEMINI_API_KEY environment variable.")

        self.client = genai.Client(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            return response.text
        except APIError as e:
            return f"Gemini API Error ({e.code}): {e.message}"
        except Exception as e:
            return f"Unexpected connection error: {str(e)}"

    def analyze_logs(self, raw_logs: str) -> str:
        if not raw_logs or not raw_logs.strip():
            raise ValueError("Logs content cannot be empty.")

        prompt = (
            "Analyze the following logs. For each error, list ONLY: "
            "1. Błąd, 2. Przyczyna, 3. Możliwa naprawa. "
            "Do not add any introductions or summaries.\n\n"
            f"--- LOGS ---\n{raw_logs}\n------------"
        )

        return self.generate_response(prompt)