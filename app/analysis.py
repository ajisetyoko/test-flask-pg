from transformers import pipeline
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model.base import History

class SentimentAnalysis():
    def __init__(self, app: Flask, db:SQLAlchemy) -> None:
        self.app = app
        self.db = db
        self.inferencer = pipeline('sentiment-analysis')
        self.app.logger.info("Sentiment Analysis is successfully intialized")

    def sentiment_analysis(self, input: str) -> str:
        resp = self.inferencer(input)
        self.save_to_db(input, resp[0])
        return resp[0]
    
    def save_to_db(self, input, resp):
        history = History(
            input_msg = input,
            label = resp['label'],
            score = resp['score']
        )
        self.db.session.add(history)
        self.db.session.commit()
        return None

    def get_all_history(self):
        data = self.db.session.query(History).all()
        return [{
            'input': d.input_msg,
            'label': d.label 
            } for d in data]