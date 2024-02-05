from flask import Flask
from config import Config
from app.extensions import db
from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # instilize flask extention here 
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    @app.route('/test/')
    def test():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
