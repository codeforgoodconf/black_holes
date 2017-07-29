from app.db import db, Galaxy
from random import randint

def add_galaxy(file_url,human_label=None,tf_label=None):
    galaxy = Galaxy(file_url,human_label,tf_label)
    db.session.add()

def update_human_label(id, human_label):
   return db.session.query(Galaxy).filter_by(id=id).update({"human_label": human_label})

def rand_galaxy():
    galaxy = Galaxy.query.get(randint(1, len(Galaxy.query.all())))
    return galaxy

