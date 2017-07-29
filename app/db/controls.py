from app.bd.__init__.py import db, Galaxy

def update_human_label(id,new_label):
    db.session.query(Galaxy)

def add_galaxy(file_url,human_label=Null,tf_label=Null):
    galaxy = Galaxy(file_url,human_label,tf_label)
    db.session.add()