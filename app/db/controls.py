from app.db.__init__.py import db, Galaxy
from random import randint

def update_human_label(id,new_label):
    db.session.query(Galaxy)

def add_galaxy(file_url,human_label=Null,tf_label=Null):
    galaxy = Galaxy(file_url,human_label,tf_label)
    db.session.add()

def rand_galaxy():
    galaxy = Galaxy.query.get(randint(1, len(Galaxy.query.all())))
