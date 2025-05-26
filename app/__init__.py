from flask import Flask

from .version import get_version

def create_app():
    app = Flask(__name__)
    app.config['VERSION'] = get_version()

    from .routes import main
    app.register_blueprint(main)
    
    @app.context_processor
    def inject_version():
        return dict(app_version=app.config['VERSION'])

    return app