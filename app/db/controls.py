from app.db import db, Galaxy
from random import randint


class Controller:
    def add_galaxy(self, file_url, human_label=None, tf_label=None):
        galaxy = Galaxy(file_url, human_label, tf_label)
        db.session.add(galaxy)

    def update_human_label(self, id, human_label):
        galaxy = Galaxy.query.get(id)
        galaxy.human_label = human_label
        db.session.commit()

    def rand_galaxy(self):
        galaxy = db.session.query(Galaxy).filter_by(human_label=None)[0]
        return galaxy

    def create_new_galaxy(self, path):
        galaxy = Galaxy(
            label_lower=None,
            label_upper=None,
            file_url=path,
            tf_value=None,
            tf_label=None,
            human_label=None)

        return galaxy

    def add_machine_label(self, file_url, machine_label):
        if not file_url.endswith(".fits"):
            file_url = f"{file_url}.fits"

        galaxies = db.session.query(Galaxy).filter_by(file_url=file_url)
        if galaxies.count():
            print(dir(galaxies))
            print(galaxies.count())


            galaxy = galaxies[0]
            galaxy.tf_label = machine_label
            db.session.commit()


