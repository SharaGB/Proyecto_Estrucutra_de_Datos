from flask import Flask
from flask_cors import CORS
from config import config
# Routes
from routes import Estudiantes

app = Flask(__name__)

CORS(app, resources={'*': {'origins': '*'}})

def page_not_found(e):
    return "<h1>Page not found</h1>", 404

if __name__ == "__main__":
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Estudiantes.main, url_prefix='/api/estudiantes')

    # Error handlers
    app.register_error_handler(404, page_not_found)

    app.run()
