from app import db

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_time = created = db.Column(db.DateTime, server_default=db.func.now())
    input_msg = db.Column(db.Text())
    label = db.Column(
        db.Enum(
            "POSITIVE",
            "NEGATIVE",
            name="label_types"
        )
    )
    score = db.Column(db.Float)

    def __init__(self, input_msg, label, score,  **kwargs):
        self.input_msg = input_msg
        self.label = label
        self.score = score