import os

from flask import Flask, jsonify
from flaskr.db import get_db

def create_app(test_config=None):
    # create & config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET'])
    def hello_world():
        return "Hi, I'm the ROOT of the app"

    @app.route('/api/v1/strategists', methods=['GET'])
    def api_get_strategists():
        db = get_db()
        strategists = db.execute('SELECT * FROM strategists')
        resp = [dict(s) for s in strategists]
        return jsonify({"data": resp, "aod_total": sum_aod(resp)})

    from . import db
    db.init_app(app)

    return app


# helpers
def sum_aod(strategists):
    total = 0
    for s in strategists:
        total += dict(s)['aod']

    return total