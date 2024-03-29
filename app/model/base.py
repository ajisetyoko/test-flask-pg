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