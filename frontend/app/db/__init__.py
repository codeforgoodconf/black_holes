from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(225))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(225), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Setup Flask_Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email="test@test.com", password="password")
    db.session.commit()


class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    label_lower = db.Column(db.Float)
    label_upper = db.Column(db.Float)
    file_url = db.Column(db.String)
    tf_value = db.Column(db.Float)
    tf_label = db.Column(db.Boolean)
    human_label = db.Column(db.Boolean)


    def __init__(self, label_lower, label_upper, file_url, tf_value, tf_label, human_label):
        self.label_lower = label_lower
        self.label_upper = label_upper
        self.file_url = file_url
        self.tf_value = tf_value
        self.tf_label = tf_label
        self.human_label = human_label

    def __repr__(self):
        return '<Galaxy %r>' % self.file_url
