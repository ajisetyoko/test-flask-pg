from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)

DB_URI = "postgresql://postgres:postgres@data-db:5432/postgres"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from model import *
from analysis import SentimentAnalysis
analysis = SentimentAnalysis(app, db)

@app.route('/')
def hello():
    return "OK"

@app.route('/analysis', methods=['POST', 'GET'])
def get_user():
    if request.method == "POST":
        payload = request.get_json()
        app.logger.info("Payload: {}".format(payload))
        inp = payload.get("text", None)
        if inp is None:
            return 401, "text input is required"
        resp = analysis.sentiment_analysis(inp)
        return jsonify(data=resp)
    else:
        return jsonify(data=analysis.get_all_history())

if __name__ == '__main__':
    app.run()