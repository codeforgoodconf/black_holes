from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label_lower = db.Column(db.Float)
    label_upper = db.Column(db.Float)
    file_url = db.Column(db.String)
    tf_value = db.Column(db.Float)
    tf_label = db.Column(db.Boolean)
    human_confirmation = db.Column(db.Boolean)
    human_label = db.Column(db.Boolean)

    def __init__(self, label_lower, label_upper, file_url, tf_value, tf_label, human_label, human_confirmation=None):
        self.human_confirmation = human_confirmation
        self.label_lower = label_lower
        self.label_upper = label_upper
        self.file_url = file_url
        self.tf_value = tf_value
        self.tf_label = tf_label
        self.human_label = human_label

    def __repr__(self):
        return '<Galaxy %r>' % self.file_url
