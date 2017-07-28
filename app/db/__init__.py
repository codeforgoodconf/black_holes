from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key = true)
    label_lower = db.Column(db.Float)
    label_upper = db.Column(db.Float)
    file_url = db.Column(db.String)
    tf_label = db.Column(db.Boolean)
    human_label = db.Column(db.Boolean)

    def __init__(self, label_lower, labe_upper, file_url, tf_label, human_label):
        self.label_lower = label_lower
        self.label_upper = label_upper
        self.file_url = file_url
        self.tf_label = tf_label
        self.human_label = human_label

    def __repr__(self):
        return '<Galaxy %r>' % self.file_url
