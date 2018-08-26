import os
from flask import Flask
from flask_restful import Api
from config.config import app_config
from resources.item import Item
from db.db import db

def create_app(env):
    flask_app = Flask(__name__)
    flask_app.config.from_object(app_config[env])

    db.init_app(flask_app)
    api = Api(flask_app)
    api.prefix = '/api'
    api.add_resource(Item, '/item/<string:name>')
    return flask_app

CONFIG = os.getenv('FLASK_ENV', default='development')
app = create_app(CONFIG)



if __name__ == '__main__':
    app.run()
