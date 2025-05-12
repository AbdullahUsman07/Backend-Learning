
from flask import Flask
from app.db import init_db
from app.routes import routes_bp
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    init_db(app)
    
    app.register_blueprint(routes_bp,url_prefix = '/api')
    
    return app