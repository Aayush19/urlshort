from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'ha54dasd4as5d1a3a654fa65s4faf4a654fa6s54f6a5sfa5s4f6af6a4fa4a64f'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app
