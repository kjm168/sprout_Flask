from flask import Flask
from app.route import hello_world, index, index_1
def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', '/', hello_world)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/index_1', 'index_1', index_1)
    return app