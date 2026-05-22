from flask import Blueprint, request, jsonify
from src.models.gemini_model import GeminiModel

gemini_blueprint = Blueprint('gemini', __name__)
gemini_model = GeminiModel()

@gemini_blueprint.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'logs' not in data:
        return jsonify({'error': 'No logs provided'}), 400
    
    logs = data['logs']
    try:
        analysis = gemini_model.analyze_logs(logs)
        return jsonify({'analysis': analysis}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
