import os
from flask import Flask
from src.controllers.main_controller import main_template
from src.controllers.gemini_controller import gemini_blueprint

BASE_DIR = os.path.dirname(__file__)
template_dir = os.path.join(BASE_DIR, 'view', 'templates')
static_dir = os.path.join(BASE_DIR, 'view', 'static')

app = Flask(
    __name__,
    template_folder=template_dir,
    static_folder=static_dir
)

app.register_blueprint(main_template)
app.register_blueprint(gemini_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
