__author__ = 'mithunmohan'

from flask import Flask
from flask_redis import FlaskRedis
from mockredis import MockRedis

def create_app(test=None):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object('config')
    from model import db
    db.init_app(app)
    #from model import redis_con
    if test is not None:
        app.redis_con = FlaskRedis.from_custom_provider(MockRedis)
        app.redis_con.init_app(app)
    else:
        app.redis_con = FlaskRedis(app)
        app.redis_con.init_app(app)
    from app.views import rest
    app.register_blueprint(rest)
    return app
