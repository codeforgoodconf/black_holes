from app.db import db, Galaxy
from random import randint


class Controller:
    def add_galaxy(self, file_url, human_label=None, tf_label=None):
        galaxy = Galaxy(file_url, human_label, tf_label)
        db.session.add(galaxy)

    def update_human_label(self, id, human_label):
        galaxy = Galaxy.query.get(id)

        print(f"Previous label: {galaxy.human_label}")
        galaxy.human_label = human_label == "True"

        print(f"New label: {galaxy.human_label}")

        db.session.add(galaxy)
        db.session.commit()

        galaxy = Galaxy.query.get(id)
        print(f"Confirm label still : {galaxy.human_label}")

    def update_machine_affirmation(self, id, affirmation):
        pass


    def rand_galaxy(self):
        galaxies = db.session.query(Galaxy).filter_by(human_label=None)
        galaxy = galaxies[randint(0,30)] #when we have all data change 30 to 400 or something bigger
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

    def add_machine_label(self, file_url, machine_prediction):
        if file_url.endswith(".fits"):
            file_url = file_url.replace(".fits", "")

        galaxies = db.session.query(Galaxy).filter_by(file_url=file_url)
        if galaxies.count():
            print(dir(galaxies))
            print(galaxies.count())

            galaxy = galaxies[0]

            galaxy.tf_label = machine_prediction > 0.8
            galaxy.tf_value = machine_prediction
            db.session.commit()


