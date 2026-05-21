from flask import Blueprint, render_template

main_template = Blueprint('main', __name__)

@main_template.route('/')
def index():
    return render_template('index.html')

@main_template.route('/api/health')
def health():
    return {'status': 'ok'}, 200
